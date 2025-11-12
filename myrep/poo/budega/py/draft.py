class Person:
    def __init__(self, name: str) -> None:
        self.name = name

    def __str__(self) -> str:
        return self.name
    

class Market:
    def __init__(self, counter_size: int) -> None:
        self.counter: list[Person | None] = [None for _ in range(counter_size)]
        self.waiting: list[Person] = []

    def arrive(self, person: Person):
        self.waiting.append(person)

    def call(self, index: int):
        if index < 0 or index >= len(self.counter):
            print('fail: caixa inexistente')
            return
        if len(self.waiting) == 0:
            print('fail: sem clientes')
            return
        if self.counter[index] is not None:
            print('fail: caixa ocupado')
            return
        self.counter[index] = self.waiting.pop(0)

    def finish(self, index: int) -> Person | None: 
        if index < 0 or index >= len(self.counter):
            print('fail: caixa inexistente')
            return None
        if self.counter[index] is None:
            print('fail: caixa vazio')
            return None
        aux = self.counter[index]
        self.counter[index] = None
        return aux
    
    def __str__(self) -> str:
        caixas = ', '.join([('-----' if x is None else str(x)) for x in self.counter])
        espera = ', '.join([str(x) for x in self.waiting])
        return f'Caixas: [{caixas}]\nEspera: [{espera}]'


def main():
    market = Market(0)
    while True:
        line = input()
        print('$' + line)
        args = line.split(' ')

        if args[0] == 'end':
            break
        elif args[0] == 'show':
            print(market)
        elif args[0] == 'init':
            qtd = int(args[1])
            market = Market(qtd)
        elif args[0] == 'arrive':
            market.arrive(Person(args[1]))
        elif args[0] == 'call':
            market.call(int(args[1]))
        elif args[0] == 'finish':
            market.finish(int(args[1]))
        else:
            print('fail: comando invalido')
    
main()
