class Fone:
    def __init__(self, id: str, number: str):
        self.__id = id
        self.__number = number

    def isValid(number: str) -> bool:
        valid = '0123456789().+-'
        return all(c in valid for c in number)

    def getId(self) -> str:
        return self.__id

    def getNumber(self) -> str:
        return self.__number

    def __str__(self) -> str:
        return f'{self.__id}:{self.__number}'


class Contact:
    def __init__(self, name: str):
        self.__name = name
        self.__favorited = False
        self.__fones: list[Fone] = []

    def addFone(self, id: str, number: str) -> None:
        if not Fone.isValid(number):
            print('fail: invalid number.')
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

    def getFones(self) -> list:
        return self.__fones

    def getName(self) -> str:
        return self.__name

    def __str__(self) -> str:
        pref = '@ ' if self.__favorited else '- '
        fstr = ', '.join(str(f) for f in self.__fones)
        return f'{pref}{self.__name} [{fstr}]'


class Agenda:
    def __init__(self):
        self.__contacts: list[Contact] = []

    def findPosByName(self, name: str) -> int:
        for i, cont in enumerate(self.__contacts):
            if cont.getName() == name:
                return i
        return -1

    def addContact(self, name: str, fones: list[Fone]):
        pos = self.findPosByName(name)
        if pos == -1:
            new = Contact(name)
            for f in fones:
                if Fone.isValid(f.getNumber()):
                    new.addFone(f.getId(), f.getNumber())
            self.__contacts.append(new)
            self.__contacts.sort(key=lambda c: c.getName())
        else:
            c = self.__contacts[pos]
            for f in fones:
                if Fone.isValid(f.getNumber()):
                    c.addFone(f.getId(), f.getNumber())

    def getContact(self, name: str):
        pos = self.findPosByName(name)
        return None if pos == -1 else self.__contacts[pos]

    def rmContact(self, name: str):
        pos = self.findPosByName(name)
        if pos == -1:
            print('fail: contact not found.')
        else:
            self.__contacts.pop(pos)

    def search(self, pattern: str) -> list:
        res = []
        for c in self.__contacts:
            if pattern in str(c):
                res.append(c)
        return res

    def getFavorited(self):
        return [c for c in self.__contacts if c.isFavorited()]

    def getContacts(self):
        return self.__contacts

    def __str__(self) -> str:
        return '\n'.join(str(c) for c in self.__contacts)


def main():
    agenda = Agenda()

    while True:
        line = input()
        print('$' + line)
        args = line.split()

        if args[0] == 'end':
            break
        elif args[0] == 'add':
            name = args[1]
            fones = []
            for item in args[2:]:
                if ':' not in item:
                    continue
                id, num = item.split(':')
                fones.append(Fone(id, num))
            agenda.addContact(name, fones)
        elif args[0] == 'rmFone':
            name = args[1]
            index = int(args[2])
            cont = agenda.getContact(name)
            if cont:
                cont.rmFone(index)
            else:
                print('fail: contact not found.')
        elif args[0] == 'rm': # remover contato
            agenda.rmContact(args[1])
        elif args[0] == 'search': # buscar
            pattern = args[1]
            result = agenda.search(pattern)
            for c in result:
                print(c) 
        elif args[0] == 'tfav': # toggle favorito
            name = args[1]
            cont = agenda.getContact(name)
            if cont:
                cont.toogleFavorited()
            else:
                print('fail: contact not found')
        elif args[0] == 'favs': # mostrar favoritos
                for c in agenda.getFavorited():
                    print(c)
        elif args[0] == 'show': # show agenda
            print(agenda)
        else:
            print('fail.')
main()
