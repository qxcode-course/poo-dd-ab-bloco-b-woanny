class Client:
    def __init__(self, id: str, phone: int):
        self.__id = id
        self.__phone = phone

    def getId(self):
        return self.__id

    def getPhone(self):
        return self.__phone

    def __str__(self):
        return f'{self.__id}:{self.__phone}'


class Theater:
    def __init__(self, size: int):
        self.__seats: list[Client | None] = [None] * size

    def __search(self, name: str) -> int:
        for i, client in enumerate(self.__seats):
            if client is not None and client.getId() == name:
                return i
        return -1

    def __verifyIndex(self, index: int) -> bool:
        return 0 <= index < len(self.__seats)

    def reserve(self, id: str, phone: int, index: int):
        # indice inválido
        if not self.__verifyIndex(index):
            print('fail: cadeira nao existe')
            return

        # cliente ja ta no cinema
        if self.__search(id) != -1:
            print('fail: cliente ja esta no cinema')
            return

        # cadeira ocupada
        if self.__seats[index] is not None:
            print('fail: cadeira ja esta ocupada')
            return

        # reserva
        self.__seats[index] = Client(id, phone)

    def cancel(self, id: str):
        pos = self.__search(id)
        if pos == -1:
            print('fail: cliente nao esta no cinema')
            return

        self.__seats[pos] = None

    def getSeats(self):
        return self.__seats

    def __str__(self):
        output = []
        for seat in self.__seats:
            if seat is None:
                output.append('-')
            else:
                output.append(str(seat))
        return '[' + ' '.join(output) + ']'

def main():
    theater = Theater(0)

    while True:
        line = input()
        print('$' + line)
        args = line.split()

        if args[0] == 'end':
            break
        elif args[0] == 'init':
            theater = Theater(int(args[1]))
        elif args[0] == 'show':
            print(theater)
        elif args[0] == 'reserve':
            theater.reserve(args[1], int(args[2]), int(args[3]))
        elif args[0] == 'cancel':
            theater.cancel(args[1])
        else:
            print('fail: comando invalido')


main()
