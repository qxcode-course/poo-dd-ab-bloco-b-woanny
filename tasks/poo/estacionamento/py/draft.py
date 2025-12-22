class Veiculo:
    def __init__(self, id, entrada):
        self.id = id
        self.entrada = entrada
        self.tipo = self.__class__.__name__

    def calcularValor(self, saida):
        pass

    def toString(self):
        return (
            self.tipo.rjust(10, '_')
            + ' : '
            + self.id.rjust(10, '_')
            + ' : '
            + str(self.entrada)
        )

class Bike(Veiculo):
    def calcularValor(self, saida):
        return 3.00


class Moto(Veiculo):
    def calcularValor(self, saida):
        tempo = saida - self.entrada
        return tempo / 20


class Carro(Veiculo):
    def calcularValor(self, saida):
        tempo = saida - self.entrada
        valor = tempo / 10
        if valor < 5:
            return 5.00
        return valor


class Estacionamento:
    def __init__(self):
        self.veiculos = {}
        self.tempoAtual = 0

    def tempo(self, valor):
        self.tempoAtual += int(valor)

    def pagar(self, id):
        veiculo = self.veiculos[id]
        saida = self.tempoAtual
        valor = veiculo.calcularValor(saida)
        print(
            f'{veiculo.tipo} chegou {veiculo.entrada} saiu {saida}. '
            f'Pagar R$ {valor:.2f}'
        )
        del self.veiculos[id]

    def estacionar(self, tipo, id):
        if tipo == 'bike':
            veiculo = Bike(id, self.tempoAtual)
        elif tipo == 'moto':
            veiculo = Moto(id, self.tempoAtual)
        elif tipo == 'carro':
            veiculo = Carro(id, self.tempoAtual)
        else:
            return
        self.veiculos[id] = veiculo

    def show(self):
        for v in self.veiculos.values():
            print(v.toString())
        print('Hora atual:', self.tempoAtual)


def main():
    est = Estacionamento()

    while True:
        line = input()
        print('$' + line)
        args = line.split()

        if args[0] == 'end':
            break

        elif args[0] == 'tempo':
            est.tempo(args[1])

        elif args[0] == 'estacionar':
            est.estacionar(args[1], args[2])

        elif args[0] == 'pagar':
            est.pagar(args[1])

        elif args[0] == 'show':
            est.show()


main()