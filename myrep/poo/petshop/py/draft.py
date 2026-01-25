class Pet:
    def __init__(self, idPet, especie):
        self.idPet = idPet
        self.especie = especie


class Client:
    def __init__(self, idClient, nome):
        self.idClient = idClient
        self.nome = nome
        self.pets = {}
        self.petCounter = 0

    def addPet(self, idPet, especie):
        if idPet in self.pets:
            raise Exception(f'animal {idPet} ja existe')
        self.petCounter += 1
        self.pets[idPet] = (self.petCounter, Pet(idPet, especie))

    def getPet(self, idPet):
        return self.pets.get(idPet, None)

    def __str__(self):
        out = f'{self.idClient}: {self.nome}'
        for _, (pid, pet) in self.pets.items():
            out += f'[{pid}:{pet.idPet}:{pet.especie}]'
        return out


class Service:
    def __init__(self, idService, price):
        self.idService = idService
        self.price = price

    def __str__(self):
        return f'{self.idService}:{self.price}'


class Sale:
    def __init__(self, idSale, idClient, idPet, idService):
        self.idSale = idSale
        self.idClient = idClient
        self.idPet = idPet
        self.idService = idService

    def __str__(self):
        return f'{self.idSale}:{self.idClient}:{self.idPet}:{self.idService}'


class Clinic:
    def __init__(self):
        self.repClients = {}
        self.repServices = {}
        self.repSales = {}
        self.nextSaleId = 0

    # Clients
    def addClient(self, idClient, nome):
        if idClient in self.repClients:
            return
        self.repClients[idClient] = Client(idClient, nome)

    def getClient(self, idClient):
        return self.repClients.get(idClient, None)

    def delClient(self, idClient):
        if idClient in self.repClients:
            del self.repClients[idClient]

    def listClients(self):
        for client in self.repClients.values():
            print(client)

    # Pets
    def addPet(self, idClient, idPet, especie):
        client = self.getClient(idClient)
        if client is None:
            print(f'fail: cliente {idClient} nao existe')
            return

    # Services
    def addService(self, idService, price):
        self.repServices[idService] = Service(idService, price)

    def getService(self, idService):
        return self.repServices.get(idService, None)

    def listServices(self):
        for service in self.repServices.values():
            print(service)

    # Sales
    def sell(self, idClient, idPet, idService):
        client = self.getClient(idClient)
        if client is None:
            print(f'fail: cliente {idClient} nao existe')
            return

        if client.getPet(idPet) is None:
            print(f'fail: animal {idPet} nao existe')
            return

        service = self.getService(idService)
        if service is None:
            print(f'fail: servico {idService} nao existe')
            return

        sale = Sale(self.nextSaleId, idClient, idPet, idService)
        self.repSales[self.nextSaleId] = sale
        self.nextSaleId += 1

    def listSales(self):
        for sale in self.repSales.values():
            print(sale)

    def balance(self):
        total = 0.0
        for sale in self.repSales.values():
            total += self.repServices[sale.idService].price
        print(total)


def main():
    clinic = Clinic()

    while True:
        line = input()
        print('$' + line)
        args = line.split()

        if args[0] == 'end':
            break
        elif args[0] == 'addcli':
            clinic.addClient(args[1], ' '.join(args[2:]))
        elif args[0] == 'getcli':
            client = clinic.getClient(args[1])
            if client:
                print(f'{client.idClient}:{client.nome}')
        elif args[0] == 'delcli':
            clinic.delClient(args[1])
        elif args[0] == 'show':
            clinic.listClients()
        elif args[0] == 'addpet':
            clinic.addPet(args[1], args[2], args[3])
        elif args[0] == 'addser':
            clinic.addService(args[1], float(args[2]))
        elif args[0] == 'listser':
            clinic.listServices()
        elif args[0] == 'sell':
            clinic.sell(args[1], args[2], args[3])
        elif args[0] == 'listsell':
            clinic.listSales()
        elif args[0] == 'balance':
            clinic.balance()
        else:
            print('fail')
main()
