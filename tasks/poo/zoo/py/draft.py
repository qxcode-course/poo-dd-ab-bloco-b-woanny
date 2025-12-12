class Animal:
    def __init__(self, nome: str):
        self.__nome = nome

    def apresentar_nome(self):
        print(f"Eu sou o(a) {self.__nome}!")

    def get_nome(self):
        return self.__nome

    def apresentar(self):
        self.apresentar_nome()
        self.fazer_som()
        self.mover()
        print(f"Objeto: {type(self).__name__}")
    
class Leao(Animal):
    def __init__(self, nome: str):
        super().__init__(nome)

    def fazer_som(self):
        print("Roooaaar!")

    def mover(self):
        print(f"{self.get_nome()} está correndo.")

class Elefante(Animal):
    def __init__(self, nome: str):
        super().__init__(nome)

    def fazer_som(self):
        print("Barulho de elefante q n sei como é.")

    def mover(self):
        print(f"{self.get_nome()} está caminhando.")

class Cobra(Animal):
    def __init__(self, nome: str):
        super().__init__(nome)

    def fazer_som(self):
        print("Ssssss...")

    def mover(self):
        print(f"{self.get_nome()} está rastejando.")
    

napoleao = Leao("Napoleão")
napoleao.apresentar_nome()
napoleao.fazer_som()
napoleao.mover()
napoleao.apresentar()

carlos = Elefante("Carlos")
carlos.apresentar_nome()
carlos.fazer_som()
carlos.mover()
carlos.apresentar()

venenosa = Cobra("Venenosa")
venenosa.apresentar_nome()
venenosa.fazer_som()
venenosa.mover()
venenosa.apresentar()