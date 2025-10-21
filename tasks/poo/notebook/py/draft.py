class Notebook:
    def __init__(self):
        self.__ligado: bool = False #True = Ligado False = Desligado

    def ligar(self):
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
        print(f'Status: {status}')

    def usar(self, tempo):
        if not self.__ligado:
            print('erro: ligue o notebook primeiro')
        else:
            print(f'Usando por {tempo} minutos')

notebook = Notebook() # criando notebook
notebook.mostrar()    # msg: Status: Desligado
notebook.usar(10)     # msg: erro: ligue o notebook primeiro
notebook.ligar()      # msg: notebook ligado
notebook.ligar()      # msg: notebook ligado
notebook.mostrar()    # msg: Status: Ligado
notebook.usar(10)     # msg: Usando por 10 minutos
notebook.desligar()   # msg: notebook desligado
notebook.desligar()   # msg: notebook desligado