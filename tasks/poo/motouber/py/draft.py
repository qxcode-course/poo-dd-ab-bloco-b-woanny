class Pessoa:
    def __init__(self, nome: str, dinheiro: int):
        self.__nome = nome
        self.__dinheiro = dinheiro

    def getNome(self):
        return self.__nome
    
    def getDinheiro(self):
        return self.__dinheiro

    def gastar(self, valor: int):
        if valor > self.__dinheiro:
            valor = self.__dinheiro
            self.__dinheiro = 0
        else:
            self.__dinheiro -= valor
        return valor
    
    def receber(self, valor:int):
        self.__dinheiro += valor

    def __str__(self):
        return f"{self.__nome}:{self.__dinheiro}"

class Moto:
    def __init__(self, custo = 0, motorista = None, passageiro = None):
        self.__custo = custo
        self.__motorista = motorista
        self.__passageiro = passageiro

    def setMotorista(self, nome, dinheiro):
        self.__motorista = Pessoa(nome,dinheiro)

    def setPassageiro(self, nome, dinheiro):
        if self.__motorista == None:
            print('fail: no driver')
            return
        self.__passageiro = Pessoa(nome, dinheiro)

    def dirigir(self, distancia):
        if self.__motorista == None:
            print('fail: no driver.')
            return
        if self.__passageiro == None:
            print('fail: no passanger')
            return

        self.__custo += distancia

    def liberarPass(self):
        if self.__passageiro == None:
            print('fail: no passenger')
            return
        
        pago = self.__passageiro.gastar(self.__custo)

        if pago < self.__custo:
            print('fail: Passenger does not have enough money')

        self.__motorista.receber(self.__custo)
        print(f'{self.__passageiro.getNome()}:{self.__passageiro.getDinheiro()} left')
        self.__custo = 0
        self.__passageiro = None

    def __str__(self):
        mot = "None" if self.__motorista == None else str(self.__motorista)
        pas = "None" if self.__passageiro == None else str(self.__passageiro)
        return f"Cost: {self.__custo}, Driver: {mot}, Passenger: {pas}"

def main():
    moto = Moto()
    while True:
        line = input()
        print('$' + line)
        args = line.split()

        if args[0] == 'end':
            break
        elif args[0] == 'show':
            print(moto)
        elif args[0] == 'setDriver':
            nome = args[1]
            dinheiro = int(args[2])
            moto.setMotorista(nome, dinheiro)
        elif args[0] == 'setPass':
            nome = args[1]
            dinheiro = int(args[2])
            moto.setPassageiro(nome, dinheiro)
        elif args[0] == 'leavePass':
            moto.liberarPass()
        elif args[0] == 'drive':
            distancia = int(args[1])
            moto.dirigir(distancia)
        else:
            print('error')
main()