class Crianca:
    def __init__(self, nome: str, idade: int):
        self.__nome = nome
        self.__idade = idade

    def getNome(self):
        return self.__nome
    
    def getIdade(self):
        return self.__idade
    
    def __str__(self):
        return f'{self.__nome}:{self.__idade}'

class Pula_Pula:
    def __init__(self):
        self.__esperando: list[Crianca] = []
        self.__pulando: list[Crianca] = []

    def arrive(self, nome:str, idade: int):
        self.__esperando.insert(0, Crianca(nome, idade))

    def enter(self):
        if len(self.__esperando) == 0:
            return
        crianca = self.__esperando.pop()
        self.__pulando.insert(0, crianca)

    def remove(self, nome: str):
        for i, crianca in enumerate(self.__esperando):
            if crianca.getNome() == nome:
                self.__esperando.pop(i)
                return
        for i, crianca in enumerate(self.__pulando):
            if crianca.getNome() == nome:
                self.__pulando.pop(i)
                return
        print(f'fail: {nome} nao esta no pula-pula')

    def show(self):
        fila = ', '.join(str(x) for x in self.__esperando)
        pula = ', '.join(str(x) for x in self.__pulando)
        print(f'[{fila}] => [{pula}]')

    def leave(self):
        if len(self.__pulando) == 0:
            return
        crianca = self.__pulando.pop()
        self.__esperando.insert(0, crianca)

def main():
    pula_pula = Pula_Pula()

    while True:
        line = input()
        print('$' + line)
        args = line.split()

        if args[0] == 'end':
            break
        elif args[0] == 'arrive':
            pula_pula.arrive(args[1], int(args[2]))
        elif args[0] == 'enter':
            pula_pula.enter()
        elif args[0] == 'show':
            pula_pula.show()
        elif args[0] == 'leave':
            pula_pula.leave()
        elif args[0] == 'remove':
            pula_pula.remove(args[1])
        else:
            print('erro')

main()