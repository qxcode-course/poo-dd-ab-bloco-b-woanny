class Fone:
    def __init__(self, id: str, number: str):
        self.__id = id
        self.__number = number

    def isValid(number: str) -> bool:
        valid = '0123456789().'
        return all(c in valid for c in number)
    
    def getID(self) -> str:
        return self.__id

    def getNumber(self) -> str:
        return self.__number
    
    def __str__(self):
        return f'{self.__id}:{self.__number}'


class Contact:
    def __init__(self, name: str = ""):
        self.__name = name
        self.__favorited = False
        self.__fones: list[Fone] = []

    def addFone(self, id: str, number: str) -> None:
        if not Fone.isValid(number):
            print('fail: invalid number')
            return
        self.__fones.append(Fone(id, number))

    def rmFone(self, index: int) -> None:
        if 0 <= index < len(self.__fones):
            self.__fones.pop(index)
        else:
            print('fail')

    def toogleFavorited(self) -> None:
        self.__favorited = not self.__favorited

    def isFavorited(self) -> bool:
        return self.__favorited
    
    def getFones(self) -> list[Fone]:
        return self.__fones

    def getName(self) -> str:
        return self.__name

    def setName(self, name: str) -> None:
        self.__name = name

    def __str__(self):
        prefix = '@ ' if self.__favorited else '- '
        inside = ', '.join(str(f) for f in self.__fones)
        return f'{prefix}{self.__name} [{inside}]'


def main():
    contato = Contact()
    while True:
        line = input()
        print('$' + line)
        args = line.split()

        if args[0] == 'end':
            break
        elif args[0] == 'init':
            name = args[1]
            contato = Contact(name)
        elif args[0] == 'show':
            print(contato)
        elif args[0] == 'add':
            id = args[1]
            number = args[2]
            contato.addFone(id, number)
        elif args[0] == 'rm':
            index = int(args[1])
            contato.rmFone(index)
        elif args[0] == 'tfav':
            contato.toogleFavorited()
        else:
            print("fail")

main()