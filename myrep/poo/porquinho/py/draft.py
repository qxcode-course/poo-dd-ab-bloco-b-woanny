class Coin: # moeda 
    def __init__(self, value: float, volume: int, label: str):
        self._value = value # valor da moeda
        self._volume = volume # volume q ocupa no  cofrinho
        self._label = label  # nome

    def getValue(self) -> float:
        return self._value

    def getVolume(self) -> int:
        return self._volume

    def getLabel(self) -> str:
        return self._label

    def __str__(self) -> str:
        return f"{self._value:.2f}:{self._volume}"

class Item: # itens guardados no cofrinho
    def __init__(self, label: str, volume: int):
        self._label = label
        self._volume = volume

    def getLabel(self) -> str:
        return self._label

    def getVolume(self) -> int:
        return self._volume

    def setLabel(self, label: str):
        self._label = label

    def setVolume(self, volume: int):
        self._volume = volume

    def __str__(self) -> str:
        return f"{self._label}:{self._volume}"

# moedas
Coin.C10 = Coin(0.10, 1, "C10")
Coin.C25 = Coin(0.25, 2, "C25")
Coin.C50 = Coin(0.50, 3, "C50")
Coin.C100 = Coin(1.00, 4, "C100")

class Pig:
    def __init__(self, volumeMax: int):
        self._broken = False # estado do porquinho (intacto/quebrado)
        self._coins = [] # lista de moedas guardadas
        self._items = [] # lista de itens guardadas
        self._volumeMax = volumeMax # capacidade máxima de volume

    def addCoin(self, coin: Coin) -> bool: # adiciona moedas no porquinho
        if self._broken: # verifica se o porquinho ta quebrado ou n
            return False
        if self.getVolume() + coin.getVolume() > self._volumeMax: # verifica se tem espaço suficiente
            return False
        self._coins.append(coin) # adiciona moedas na lista
        return True

    def addItem(self, item: Item) -> bool: # adiciona itens no porquinho
        if self._broken: # verifica se o porquinho ta quebrado ou n
            return False
        if self.getVolume() + item.getVolume() > self._volumeMax: # verifica se tem espaço suficiente
            return False
        self._items.append(item) # adiciona itens na lista
        return True

    def breakPig(self): # quebra opobre porquinho pra remover suas entranhas
        if self._broken:
            return False  # marcar q ta quebrado, destruido, desvivido pra n quebrar de novo
        
        self._broken = True
        return True
    
    def extractCoins(self): # Remove e retorna todas as moedas do porquinho.
        if not self._broken:
            return None
        coins = self._coins
        self._coins = []
        return coins

    def extractItems(self): #Remove e retorna todos os itens do porquinho.
        if not self._broken:
            return None
        items = self._items
        self._items = []
        return items

    def getVolume(self) -> int: # Retorna o volume total ocupado pelo conteúdo do porquinho
        if self._broken:
            return 0
        total = 0
        for c in self._coins:
            total += c.getVolume()
        for i in self._items:
            total += i.getVolume()
        return total

    def getValue(self) -> float: #Retorna o valor total das moedas no porquinho
        total = 0.0
        for c in self._coins:
            total += c.getValue()
        return total

    def getVolumeMax(self) -> int:
        return self._volumeMax

    def isBroken(self) -> bool: # verifica se o porquinho ta quebrado
        return self._broken

    def __str__(self) -> str:
        state = "broken" if self._broken else "intact"
        coins = "[" + ", ".join(str(c) for c in self._coins) + "]"
        items = "[" + ", ".join(str(i) for i in self._items) + "]"
        value = f"{self.getValue():.2f}"
        volume = f"{self.getVolume()}/{self._volumeMax}"
        return f"state={state} : coins={coins} : items={items} : value={value} : volume={volume}"

def main():
    pig = Pig(0)
    while True:
        line = input()
        print('$' + line)
        args = line.split()

        if args[0] == "end":
            break
        elif args[0] == "init":
            pig = Pig(int(args[1]))
        elif args[0] == "show":
            print(pig)
        elif args[0] == "addCoin":
            coin_map = {
                "10": Coin.C10,
                "25": Coin.C25,
                "50": Coin.C50,
                "100": Coin.C100
            }
            if not pig.addCoin(coin_map[args[1]]):
                print("fail: the pig is broken" if pig._broken else "fail: the pig is full")
        elif args[0] == "addItem":
            item = Item(args[1], int(args[2]))
            if not pig.addItem(item):
                print("fail: the pig is broken" if pig._broken else "fail: the pig is full")
        elif args[0] == "break":
            pig.breakPig()
        elif args[0] == "extractItems":
            items = pig.extractItems()
            if items is None:
                print("fail: you must break the pig first")
                print("[]")
            else:
                print("[" + ", ".join(str(i) for i in items) + "]")
        elif args[0] == "extractCoins":
            coins = pig.extractCoins()
            if coins is None:
                print("fail: you must break the pig first")
                print("[]")
            else:
                print("[" + ", ".join(str(c) for c in coins) + "]")
        else:
            print('fail')
main()