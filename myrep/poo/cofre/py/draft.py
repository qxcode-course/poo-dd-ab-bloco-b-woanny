class Valuable: # base para coisas com valor: moedas e itens
    # métodos para serem implementados pelas filhas
    def getLabel(self): # nome do objeto
        pass

    def getValue(self): # valor em dinheiro
        pass

    def getVolume(self): # volume q ocupa no porco com esteroides
        pass

    # em teoria deve retornar label:valor:volume
    def __str__(self):
        return f'{self.getLabel()}:{self.getValue():.2f}:{self.getVolume()}'

class Coin(Valuable): # filha moeda 
    def __init__(self, value, volume, label):
        self._value = value
        self._volume = volume
        self._label = label

    def getLabel(self):
        return self._label
    
    def getValue(self):
        return self._value
    
    def getVolume(self):
        return self._volume
    
# criação das moedas
Coin.M10 = Coin('M10', 0.10, 1)
Coin.M25 = Coin('M25', 0.25, 2)
Coin.M50 = Coin('M50', 0.50, 3)
Coin.M100 = Coin('M100', 1.00, 4)

class Item(Valuable):# itens guardados no cofrinho
    def __init__(self, label, volume, value):
        self._label = label      # nome do item
        self._volume = volume    # volume que ocupa
        self._value = value      # valor monetário do item

    # métodos do Valuable
    def getLabel(self):
        return self._label
    
    def getValue(self):
        return self._value
    
    def getVolume(self):
        return self._volume
    
    # alterar propriedades do item
    def setLabel(self, label):
        self._label = label
    
    def setVolume(self, volume):
        self._volume = volume
     
class Pig:
    def __init__(self, volumeMax):
        self._broken = False      # estado do porquinho (intacto/quebrado)
        self._valuables = []      # lista de objetos de valor guardados
        self._volumeMax = volumeMax  # capacidade máxima de volume

    def addValuable(self, valuable): # adiciona coisas com valor no porquinho
        if self._broken: # verifica se o porquinho ta quebrado ou n
            return False
        
        if self.getVolume() + valuable.getVolume() > self._volumeMax: # verifica se tem espaço suficiente
            return False
        
        self._valuables.append(valuable)  # adiciona o objeto na lista      
        return True

    def breakPig(self): # quebra opobre porquinho pra remover suas entranhas
        if self._broken:
            return False  # marcar q ta quebrado, destruido, desvivido pra n quebrar de novo
        
        self._broken = True
        return True
    
    def getCoins(self): # pega as moedas do cofrinho só se ele tiver quebrado
        if not self._broken:
            return None # n da pra tirar dinheiro com ele fechado

        # separa as moedas dos itens
        coins = []  
        items = []
        for v in self._valuables:
            if isinstance(v, Coin):
                coins.append(v)
            else:
                items.append(v)
        
        self._valuables = items # mantem as itens remove moedas
        return coins
    
    def getItems(self): # pega os itens do porquinho se ele tiver quebrado
        if not self._broken:
            return None  # n da pra tirar item com ele fechado  

        # separa os itens das moedas
        coins = []
        items = []
        for v in self._valuables:
            if isinstance(v, Item):
                items.append(v)
            else:
                coins.append(v)
        
        self._valuables = coins # mantem as moedas remove itens
        return items 

    def calcValue(self): # calcula o valor TOTAL de tudo no porquinho
        total = 0.0
        for v in self._valuables:
            total += v.getValue()
        return total
    
    def getVolume(self): # calcula o volume TOTAL ocupado no porquinho
        if self._broken:
            return 0

        total = 0
        for v in self._valuables:
            total += v.getVolume()
        return total

    def getVolumeMax(self): # retorna a capacidade máxima do porquinho
        return self._volumeMax
    
    def isBroken(self): # verifica se o porquinho ta quebrado
        return self._broken
    
    def __str__(self): # string do estado atual do porquinho
        valuables_str = '[' + ', '.join(str(v) for v in self._valuables) + ']' # lista de objetos

        value_str = f'{self.calcValue():.2f}' # formata valor pra 2 casas decimais
        
        volume_str = f'{self.getVolume()}/{self._volumeMax}' # volume atual/máximo

        status = 'broken' if self._broken else 'intact' # estado: intacto ou quebrado

        return f'{valuables_str} : {value_str}$ : {volume_str} : {status}' # [itens] : valor$ : volume/volume max : status

def main():
    pig = Pig(0)
    while True:
        line = input()
        print('$' + line)
        args = line.split()

        if args[0] == 'end':
            break
        elif args[0] == 'init':
            pig = Pig(int(args[1]))
        elif args[0] == 'show':
            print(pig)
        elif args[0] == 'addCoin':
            value = int(args[1])
            coin_map = {
                10: Coin(0.10, 1, 'M10'),
                25: Coin(0.25, 2, 'M25'),
                50: Coin(0.50, 3, 'M50'),
                100: Coin(1.00, 4, 'M100')
            }
            if not pig.addValuable(coin_map[value]):
                print('fail: the pig is broken' if pig.isBroken() else 'fail: the pig is full')
        elif args[0] == 'addItem':
            item = Item(args[1], int(args[3]), float(args[2]))
            if not pig.addValuable(item):
                print('fail: the pig is broken' if pig.isBroken() else 'fail: the pig is full')
        elif args[0] == 'break':
            pig.breakPig()
        elif args[0] == 'extractCoins':
            coins = pig.getCoins()
            if coins is None:
                print('fail: you must break the pig first')
            else:
                print('[' + ', '.join(str(c) for c in coins) + ']')
        elif args[0] == 'extractItems':
            items = pig.getItems()
            if items is None:
                print('fail: you must break the pig first')
            else:
                print('[' + ', '.join(str(i) for i in items) + ']')
        else:
            print('fail')
main()