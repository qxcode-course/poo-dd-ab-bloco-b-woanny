class Lead:
    def __init__(self, calibre: float, dureza: str, tamanho: int):
        self.__calibre = calibre
        self.__dureza = dureza
        self.__tamanho = tamanho

    def getCalibre(self):
        return self.__calibre
    
    def getDureza(self):
        return self.__dureza
    
    def getTamanho(self):
        return self.__tamanho
    
    def setTamanho(self, valor):
        self.__tamanho = valor

    def usagePerSheet(self) -> int:
        gasto = {
            'HB': 1,
            '2B': 2,
            '4B': 4,
            '6B': 6
        }
        return gasto[self.__dureza]

    def __str__(self):
        return f'{self.__calibre}:{self.__dureza}:{self.__tamanho}'


class Lapiseira:
    def __init__(self, calibre: float):
        self.__calibre = calibre
        self.__bico: Lead | None = None
        self.__tambor: list[Lead] = []

    def insert(self, calibre: float, dureza: str, tamanho:int):
        if calibre != self.__calibre:
            print('fail: calibre incompatível')
            return
        self.__tambor.append(Lead(calibre, dureza, tamanho))

    def pull(self):
        if self.__bico is not None:
            print('fail: ja existe grafite no bico')
            return
        if len(self.__tambor) == 0:
            return
        self.__bico = self.__tambor.pop(0)

    def remove(self):
        if self.__bico is None:
            return
        self.__bico = None

    def write(self):
        if self.__bico is None:
            print('fail: nao existe grafite no bico')
            return

        gasto = self.__bico.usagePerSheet()

        if self.__bico.getTamanho() <= 10:
            print('fail: tamanho insuficiente')
            return
        
        if self.__bico.getTamanho() - gasto < 10:
            print('fail: folha incompleta')
            self.__bico.setTamanho(10)
            return
        
        self.__bico.setTamanho(self.__bico.getTamanho() - gasto)

    def show(self):
        bico_str = f'[{self.__bico}]' if self.__bico else '[]'
        tambor_str = ''.join([f'[{x}]' for x in self.__tambor])
        print(f'calibre: {self.__calibre}, bico: {bico_str}, tambor: <{tambor_str}>')


def main():
    lapiseira = None

    while True:
        line = input()
        print('$' + line)
        args = line.split()

        if args[0] == 'end':
            break
        elif args[0] == 'init':
            lapiseira = Lapiseira(float(args[1]))
        elif args[0] == 'show':
            lapiseira.show()
        elif args[0] == 'insert':
            lapiseira.insert(float(args[1]), args[2], int(args[3]))
        elif args[0] == 'pull':
            lapiseira.pull()
        elif args[0] == 'remove':
            lapiseira.remove()
        elif args[0] == 'write':
            lapiseira.write()
        else:
            print('erro')

main()
