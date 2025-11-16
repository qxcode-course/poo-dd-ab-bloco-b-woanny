class Player:
    def __init__(self, label: int):
        self.__label = label
        self.__pos = 0
        self.__free = True

    def getLabel(self):
        return self.__label
    
    def getPos(self):
        return self.__pos
    
    def isFree(self):
        return self.__free
    
    def setPos(self, pos: int):
        self.__pos = pos

    def setFree(self, free: bool):
        self.__free = free

    def __str__(self):
        return str(self.__label)


class Board:
    def __init__(self, nPlayers: int, boardSize: int):
        self.__players: list[Player] = [Player(x + 1) for x in range(nPlayers)]
        self.__running: bool = True
        self.__boardSize: int = boardSize
        self.__traps: set[int] = set()
        self.__current: int = 0

    def addTrap(self, pos: int):
        if 1 <= pos <= self.__boardSize:
            self.__traps.add(pos)

    def rollDice(self, value: int):
        if not self.__running:
            print('game is over')
            return
        
        player = self.__players[self.__current]
        label = player.getLabel()

        # jogador preso
        if not player.isFree():
            if value % 2 == 0:
                player.setFree(True)
                print(f'player{label} se libertou')
            else:
                print(f'player{label} continua preso')

            self.__current = (self.__current + 1) % len(self.__players)
            return

        # jogador livre
        newpos = player.getPos() + value

        # ganhou
        if newpos > self.__boardSize:
            print(f'player{label} ganhou')
            self.__running = False
            return

        # movimento normal
        player.setPos(newpos)
        print(f'player{label} andou para {newpos}')

        # caiu em armadilha
        if newpos in self.__traps:
            player.setFree(False)
            print(f'player{label} caiu em uma armadilha')

        # próximo jogador
        self.__current = (self.__current + 1) % len(self.__players)

    def toString(self) -> str:
        out = []

        for p in self.__players:
            line = ['.'] * (self.__boardSize + 1)
            pos = p.getPos()

            if 0 <= pos <= self.__boardSize:
                if line[pos] == '.':
                    line[pos] = str(p.getLabel())
                else:
                    line[pos] = line[pos] + str(p.getLabel())

            out.append(f'player{p.getLabel()}: ' + ''.join(line))

        traps_line = ''.join('x' if i in self.__traps else '.' 
                            for i in range(self.__boardSize + 1))

        out.append('traps__: ' + traps_line)
        return '\n'.join(out)

    def show(self):
        print(self.toString())


def main():
    board = None

    while True:
        line = input()
        print('$' + line)
        args = line.split()

        if args[0] == 'end':
            break
        if args[0] == 'init':
            nPlayers = int(args[1])
            boardSize = int(args[2])
            board = Board(nPlayers, boardSize)
        elif args[0] == 'show':
            if board:
                board.show()
            else:
                print('board not initialized')
        elif args[0] == 'addTrap':
            if board:
                pos = int(args[1])
                board.addTrap(pos)
        elif args[0] == 'roll':
            if board:
                value = int(args[1])
                board.rollDice(value)
        else:
            print('erro')
main()