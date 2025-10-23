class Notebook:
    def __init__(self):
        self.__ligado: bool = False #True = Ligado False = Desligado
        self.__bateria: Bateria | None = None

    def ligar(self):
        if self.__bateria is None or self.__bateria.getCarga() == 0:
            print('não foi possível ligar')
        
        if not self.__ligado: # se não for falso é verdadeiro e verdadeiro é ligado
            self.__ligado = True
            print('notebook ligado')
        else:
            print('notebook já está ligado')

    def desligar(self):
        if self.__ligado: # se for falso é falso e falso é desligado
            self.__ligado = False
            print ('notebook desligado')
        else:
            print ('notebook já está desligado')

    def mostrar(self):
        status = 'Ligado' if self.__ligado else 'Desligado'
        
        if self.__bateria is None:
            print(f'Status: {status}, Bateria: Nenhuma')
        else:
            print(f'Status: {status}, Bateria: ({self.__bateria.getCarga()}/{self.__bateria.getCapacidade()})')

    def usar(self, tempo):
        if not self.__ligado:
            print('erro: ligue o notebook primeiro')
            return
        
        if self.__bateria is None:
            print('não foi possível ligar')
            return

        tempo_usado = self.__bateria.consumir(tempo)

        print(f'Usando por {tempo_usado} minutos')

        if self.__bateria.getCarga() == 0:
            self.desligar()

    def setBateria(self, bateria):
        self.__bateria = bateria

    def rmBateria(self):
        if self.__bateria is None:
            print('já está sem bateria')
            return None
        else:
            print('bateria removida')
            bateria = self.__bateria
            self.__bateria = None
            return bateria

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
        
notebook = Notebook() # criando notebook
notebook.mostrar()    # msg: Status: Desligado, Bateria: Nenhuma
notebook.usar(10)     # msg: erro: ligue o notebook primeiro
notebook.ligar()      # msg: não foi possível ligar
notebook.mostrar()    # msg: Status: Desligado, Bateria: Nenhuma
bateria = Bateria(50) # criando bateria que suporta 50 minutos e começa carregada
bateria.mostrar()     # (50/50)
notebook.setBateria(bateria) # coloca a bateria no notebook
notebook.mostrar()    # msg: Status: Desligado, Bateria: (50/50)
notebook.usar(10)     # msg: notebook desligado
notebook.ligar()      # msg: notebook ligado
notebook.mostrar()    # msg: Status: Ligado, Bateria: (50/50)
notebook.usar(30)     # msb: Usando por 30 minutos
notebook.mostrar()    # msg: Status: Ligado, Bateria: (20/50)
notebook.usar(30)     # msb: Usando por 20 minutos, notebook descarregou
notebook.mostrar()    # msg: Status: Desligado, Bateria: (0/50)
notebook.ligar()      # msg: não foi possível ligar
bateria = notebook.rmBateria() # msg: bateria removida
bateria.mostrar()     # (0/50)