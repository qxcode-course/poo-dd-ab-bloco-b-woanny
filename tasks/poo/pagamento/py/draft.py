class Pagamento:
    def __init__(self, valor: float, descricao: str):
        self.__valor = valor
        self.__descricao = descricao

    def get_valor(self):
        return self.__valor

    def get_descricao(self):
        return self.__descricao

    def validar_valor(self):
        if self.__valor <= 0:
            raise Exception('Valor inválido.')

    def resumo(self):
        print(f'Pagamento de R$ {self.__valor}: {self.__descricao}')

    def processar(self):
        pass

class CartaoCredito(Pagamento):
    def __init__(self, valor, descricao, numero, nome_titular, limite_disponivel):
        super().__init__(valor, descricao)

        self.__numero = numero
        self.__nome_titular = nome_titular
        self.__limite = limite_disponivel

    def processar(self):
        if self.get_valor() > self.__limite:
            raise Exception(f'Limite insuficiente no cartão {self.__numero}')
        self.__limite -= self.get_valor()
        print(f'Pagamento aprovado no cartão {self.__nome_titular}. Limite restante: {self.__limite}')

class Pix(Pagamento):
    def __init__(self, valor, descricao, chave, banco):
        super().__init__(valor, descricao)
        self.__chave = chave
        self.__banco = banco

    def processar(self):
        print(f'PIX enviado via {self.__banco} usando chave {self.__chave}')


class Boleto(Pagamento):
    def __init__(self, valor, descricao, codigo_barras, vencimento):
        super().__init__(valor, descricao)
        self.__codigo_barras = codigo_barras
        self.__vencimento = vencimento

    def processar(self):
        print('Boleto gerado. Aguardando pagamento...')

print('> Pix')

pix = Pix(150, 'Camisa', 'email@ex.com', 'Banco X')
pix.resumo()
pix.validar_valor()
pix.processar()

print('> Cartão')

cartao = CartaoCredito(400, 'Tênis', '1234 5678 9123 4567', 'Cliente X', 500)
cartao.resumo()
cartao.validar_valor()
cartao.processar()

print('> Boleto')

pag3 = Boleto(89.90, 'Livro', '123456789000', '9/12/2025')
pag3.resumo()
pag3.validar_valor()
pag3.processar()