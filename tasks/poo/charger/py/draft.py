class Notebook:
    def __init__(self):
        self.__ligado: bool = False # True = Ligado False = Desligado
        self.__bateria: Bateria | None = None
        self.__carregador: Carregador | None = None 
        self.__tempo_ligado = 0  # não foi usado ainda

    def mostrar(self):
        status = 'Ligado' if self.__ligado else 'Desligado'
        
        bateria_str = 'Nenhuma' if self.__bateria == None else f'({self.__bateria.getCarga()}/{self.__bateria.getCapacidade()})'
        carregador_str = 'Desconhecido' if self.__carregador == None else f'(Potência {self.__carregador.getPotencia()})'
        print(f'Status: {status}, Bateria: {bateria_str}, Carregador: {carregador_str}')

    def ligar(self):
        if self.__ligado: # se for falso é falso e falso é desligado
            print('notebook já está ligado')
            return

        if (self.__bateria == None or self.__bateria.getCarga() == 0) and self.__carregador == None:
            print('não foi possível ligar')
            return

        self.__ligado = True
        print('notebook ligado')

    def desligar(self):
        if self.__ligado:
            self.__ligado = False
            print('notebook desligado')
        else:
            print('notebook já está desligado')

    def usar(self, tempo):
        if not self.__ligado:
            print('erro: ligue o notebook primeiro')
            return

        # Caso tenha apenas o carregador (sem bateria)
        if self.__bateria == None and self.__carregador != None:
            print('Notebook utilizado com sucesso')
            return

        # Caso tenha bateria mas sem carregador
        if self.__bateria != None and self.__carregador == None:
            tempo_usado = self.__bateria.consumir(tempo)
            print(f'Usando por {tempo_usado} minutos')
            if self.__bateria.getCarga() == 0:
                print('notebook descarregou')
                self.desligar()
            return

        # Caso tenha bateria e carregador
        if self.__bateria != None and self.__carregador != None:
            # enquanto usa, a bateria carrega (mesmo tempo de uso)
            self.__bateria.carregar(self.__carregador.getPotencia() * tempo)
            print('Notebook utilizado com sucesso')
            return

        # Caso não tenha bateria nem carregador
        print('erro: sem bateria e sem carregador')

    def setBateria(self, bateria):
        self.__bateria = bateria

    def rmBateria(self):
        if self.__bateria == None:
            print('já está sem bateria')
            return None
        else:
            print('bateria removida')
            bateria = self.__bateria
            self.__bateria = None
            return bateria

    def setCarregador(self, carregador):
        self.__carregador = carregador

    def rmCarregador(self):
        if self.__carregador == None:
            print('já está sem carregador')
            return None
        else:
            print('carregador removido')
            carregador = self.__carregador
            self.__carregador = None
            return carregador

class Bateria:
    def __init__(self, capacidade):
        self.__capacidade: int = capacidade
        self.__carga: int = capacidade  # iniciar a carga com a capacidade

    def mostrar(self):
        print(f'({self.__carga}/{self.__capacidade})')

    def getCarga(self):
        return self.__carga
    
    def getCapacidade(self):
        return self.__capacidade

    def consumir(self, tempo):
        if tempo > self.__carga: # caso tentar usar mais tempo do que carga
            tempo_usado = self.__carga
            self.__carga = 0 # descarregou
            return tempo_usado
        else:
            self.__carga -= tempo # diminui o tempo na carga
            return tempo

    def carregar(self, quantidade):
        self.__carga += quantidade
        if self.__carga > self.__capacidade:
            self.__carga = self.__capacidade

class Carregador:
    def __init__(self, potencia):
        self.__potencia: int = potencia

    def mostrar(self):
        print(f'(Potência {self.__potencia})')

    def getPotencia(self):
        return self.__potencia