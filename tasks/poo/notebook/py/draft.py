class Notebook:
    def __init__(self):
        self.__ligado: bool = False #True = Ligado False = Desligado
        self.__bateria: Bateria | None = None
        self.__carregador: Carregador | None = None

    def mostrar(self):
        status = 'Ligado' if self.__ligado else 'Desligado'
        
        bateria_str = 'Nenhuma' if self.__bateria == None else f'({self.__bateria.getCarga()}/{self.__bateria.getCapacidade()})'
        carregador_str = 'Desconhecido' if self.__carregador == None else f'(Potência {self.__carregador.getPotencia()})'
        print(f'Status: {status}, Bateria: {bateria_str}, Carregador: {carregador_str}')
    
    def ligar(self):
        if self.__ligado:
            print('notebook já está ligado')
            return

        if (self.__bateria == None or self.__bateria.getCarga() == 0) and self.__carregador == None:
            print('não foi possível ligar')
            return

        self.__ligado = True
        print('notebook ligado')

    def desligar(self):
        if self.__ligado: # se for falso é falso e falso é desligado
            self.__ligado = False
            print ('notebook desligado')
        else:
            print ('notebook já está desligado')

    def usar(self, tempo):
        if self.__carregador != None and self.__bateria != None:
            return self.__carregador.carregar()

        if not self.__ligado:
            print('erro: ligue o notebook primeiro')
            return

        tempo_usado = self.__bateria.consumir(tempo)

        print(f'Usando por {tempo_usado} minutos')

        if self.__bateria.getCarga() == 0:
            self.desligar()

    def setBateria(self, bateria):
        self.__bateria = bateria

    def rmBateria(self):
        if self.__bateria == None:
            print('já está sem bateria')
            return None
        else:
            print('bateria removida')
            self.__bateria.consumir(self.__bateria.getCarga())
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
        self.__carga: int = capacidade # iniciar a carga com a capacidade

    def mostrar(self):
        print(f'({self.__carga}/{self.__capacidade})')

    def getCarga(self):
        return self.__carga
    
    def getCapacidade(self):
        return self.__capacidade

    def consumir(self, tempo):
        if tempo > self.__carga: #caso tentar usar mais tempo do que carga
            tempo_usado = self.__carga
            self.__carga = 0 #descarregou
            return tempo_usado
        else:
            self.__carga -= tempo # diminui o tempo na carga
            return tempo

class Carregador:
    def __init__(self, potencia):
        self.__potencia: int = potencia
        self.__bateria: Bateria | None = None

    def mostrar(self):
        print(f'Potência {self.__potencia}')

    def getPotencia(self):
        return self.__potencia

    def carregar(self, tempo):
        if self.__bateria != None:
            carga_nova = self.__bateria.getCarga() + tempo * self.__potencia

        if carga_nova > self.__bateria.getCapacidade():
            carga_nova = self.__bateria.getCapacidade()
        
        return carga_nova


notebook = Notebook() # criando notebook
notebook.mostrar()    # msg: Status: Desligado, Bateria: Nenhuma, Carregador: Desconectado
notebook.ligar()      # msg: não foi possível ligar
notebook.usar(10)     # msg: notebook desligado

bateria = Bateria(50) # criando bateria que suporta 50 minutos e começa carregada
bateria.mostrar()     # (50/50)
notebook.setBateria(bateria) # coloca a bateria no notebook

notebook.mostrar() # msg: Status: Desligado, Bateria: (50/50), Carregador: Desconectado
notebook.ligar()   # msg: notebook ligado
notebook.mostrar() # msg: Status: Ligado, Bateria: (50/50), Carregador: Desconectado
notebook.usar(30)  # msb: Usando por 30 minutos
notebook.mostrar() # msg: Status: Ligado, Bateria: (20/50), Carregador: Desconectado
notebook.usar(30)  # msb: Usando por 20 minutos, notebook descarregou
notebook.mostrar() # msg: Status: Desligado, Bateria: (0/50), Carregador: Desconectado

bateria = notebook.rmBateria() # msg: bateria removida
bateria.mostrar()  # (0/50)
notebook.mostrar() # msg: Status: Desligado, Bateria: Nenhuma, Carregador: Desconectado

carregador = Carregador(2) # criando carregador com 2 de potencia
carregador.mostrar() # (Potência 2)

notebook.setCarregador(carregador) # adicionando carregador no notebook
notebook.mostrar() # msg: Status: Desligado, Bateria: Nenhuma, Carregador: (Potência 2)
notebook.ligar()   # msg: notebook ligado
notebook.mostrar() # msg: Status: Ligado, Bateria: Nenhuma, Carregador: (Potência 2)

notebook.setBateria(bateria)
notebook.mostrar() # msg: Status: Ligado, Bateria: (0/50), Carregador: (Potência 2)
notebook.usar(10)  # msg: Notebook utilizado com sucesso
notebook.mostrar() # msg: Status: Ligado, Bateria: (20/50), Carregador: (Potência 2)