class Lead:
    def __init__(self, thickness: float, hardness: str, size: int):
        self.__thickness = thickness
        self.__hardness = hardness
        self.__size = size

    def usagePerSheet(self):
        gasto = {'HB': 1, '2B': 2, '4B': 4, '6B': 6}
        return gasto[self.__hardness]
    
    def getThickness(self):
        return self.__thickness
    
    def getHardness(self):
        return self.__hardness
    
    def getSize(self):
        return self.__size
    
    def setSize(self, new_size: int):
        self.__size = new_size

    def __str__(self):
        return f"[{self.__thickness}:{self.__hardness}:{self.__size}]"


class Pencil:
    def __init__(self, thickness: float):
        self.__thickness = thickness
        self.__lead: Lead | None = None

    def hasGrafite(self):
        return self.__lead != None

    def insert(self, lead: Lead):
        if self.hasGrafite():
            print('fail: ja existe grafite')
        elif lead.getThickness() != self.__thickness:
            print('fail: calibre incompativel')
        else:
            self.__lead = lead

    def remove(self):
        if not self.hasGrafite():
            print('fail: nao existe grafite')
            return None
        lead = self.__lead
        self.__lead = None
        return lead
    
    def writePage(self):
        if not self.hasGrafite():
            print('fail: nao existe grafite')
            return

        gasto = self.__lead.usagePerSheet()
        tamanho = self.__lead.getSize()

        if tamanho <= 10:
            print('fail: tamanho insuficiente')
            return

        if tamanho - gasto < 10:
            self.__lead.setSize(10)
            print('fail: folha incompleta')
        else:
            self.__lead.setSize(tamanho - gasto)

    def __str__(self):
        grafite_str = "null" if not self.hasGrafite() else str(self.__lead)
        return f"calibre: {self.__thickness}, grafite: {grafite_str}"


def main():
    pencil: Pencil | None = None
    while True:
        line = input()
        print('$' + line)
        args = line.split()

        if args[0] == 'end':
            break
        elif args[0] == 'init':
            pencil = Pencil(float(args[1]))
        elif args[0] == 'show':
            if pencil != None:
                print(pencil)
            else:
                print('fail: lapiseira nao foi inicializada')
        elif args[0] == 'insert':
            if pencil == None:
                print('fail: lapiseira nao inicializada')
            else:
                lead = Lead(float(args[1]), args[2], int(args[3]))
                pencil.insert(lead)
        elif args[0] == 'remove':
            if pencil == None:
                print('fail: lapiseira nao foi inicializada')
            else:
                pencil.remove()
        elif args[0] == "write":
            if pencil == None:
                print("fail: lapiseira nao inicializada")
            else:
                pencil.writePage()
        else:
            print('error')

main()
