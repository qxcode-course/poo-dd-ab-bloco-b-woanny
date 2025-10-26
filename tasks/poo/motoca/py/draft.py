class Pessoa:
    def __init__(self, nome: str, idade: int):
        self.__nome = nome
        self.__idade = idade

    def getNome(self):
        return self.__nome
    
    def getIdade(self):
        return self.__idade

    def __str__(self):
        return f'{self.__nome}:{self.__idade}'


class Moto:
    def __init__(self, potencia: int = 1):
        self.__pessoa: Pessoa | None = None
        self.__potencia = potencia
        self.__time = 0

    def inserir(self, pessoa: Pessoa):
        if self.__pessoa != None:
            print('fail: busy motorcycle')
            return
        self.__pessoa = pessoa

    def remover(self):
        if self.__pessoa == None:
            print('fail: empty motorcycle')
            return
        aux = self.__pessoa
        self.__pessoa = None
        return aux

    def buyTime(self, time: int):
        self.__time += time
        
    def dirigir(self, time: int):
        if self.__time == 0:
            print('fail: buy time first')
            return
        if self.__pessoa == None:
            print('fail: empty motorcycle')
            return
        if self.__pessoa.getIdade() > 10:
            print('fail: too old to drive')
            return
        if time > self.__time:
            print(f'fail: time finished after {self.__time} minutes')
            self.__time = 0
            return
        self.__time -= time

    def honk(self):
        print("P" + ("e" * self.__potencia) + "m")

    def init(self, potencia: int):
        self.__potencia = potencia
        self.__time = 0
        self.__pessoa = None

    def __str__(self):
        pessoa_str = "(empty)" if self.__pessoa is None else f"({self.__pessoa})"
        return f"power:{self.__potencia}, time:{self.__time}, person:{pessoa_str}"


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
        elif args[0] == 'init':
            moto.init(int(args[1]))
        elif args[0] == 'enter':
            nome = str(args[1])
            idade = int(args[2])
            moto.inserir(Pessoa(nome, idade))
        elif args[0] == 'leave':
            pessoa = moto.remover()
            if pessoa != None:
                print(pessoa)
        elif args[0] == 'buy':
            moto.buyTime(int(args[1]))
        elif args[0] == 'drive':
            moto.dirigir(int(args[1]))
        elif args[0] == 'honk':
            moto.honk()
        else:
            print('error')


main()