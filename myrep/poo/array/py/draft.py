class Foo:
    def __init__(self, x: int):
        self.x = x

    def __str__(self):
        return f'Foo({self.x})'


# Array vazio
vazio: list[int] = []

# Array preenchido
preenchido: list[int] = ['Batata', 'Cenoura', 'Alface', 'Brocolis', 'Repolho', 'Rabanete']

# Array preenchido com objetos
lista_objetos: list[Foo] = [Foo(1), Foo(2), Foo(3)]

# Tamanho do array
print("Tamanho:", len(preenchido))
print('Preenchido: ',preenchido)

# Adicionar elemento no final
preenchido.append('Tomate')
print('Append Tomate: ',preenchido)

# Remover elemento no final
preenchido.pop()
print('Pop final: ',preenchido)

# Adicionar elemento no início
preenchido.insert(0, 'Banana')
print('Inset 0: ',preenchido)

# Remover elemento no início
preenchido.pop(0)
print('Pop 0: ',preenchido)

# Adicionar em uma posição específica
preenchido.insert(2, 'Cebola')
print('Insert Cebola 2: ',preenchido)

# Remover em uma posição específica
preenchido.pop(2)
print('Pop 2: ',preenchido)

# Impressão formatada usando join
print("Formatacao Join:", ", ".join(preenchido))

# Criar array com sequência de 0 a n
sequencia = list(range(0, 11))
print(sequencia)

# Criar array com valores aleatórios
import random
aleatorios = [random.randint(1, 10) for _ in range(5)]
print(aleatorios)

# Acessar elemento por índice
print("Primeiro:", sequencia[0])

# Percorrer com for-range
for item in sequencia:
    print('Percorrendo: ', item)

# Percorrer com for indexado
for i in range(len(sequencia)):
    print('Index: ', i, sequencia[i])

# Procurar elemento X manualmente
procura = "Cenoura"
encontrado = False
for item in preenchido:
    if item == procura:
        encontrado = True

# Procurar usando função nativa
print("Tem Cenoura?", procura in preenchido)

# Filtrar elementos (ex: com letra A)
filtrados = [x for x in preenchido if "a" in x.lower()]
print(filtrados)

# Transformar elementos (ex: maiúsculas)
transformados = [x.upper() for x in preenchido]

# Buscar e remover um elemento X
if "Batata" in preenchido:
    preenchido.remove("Batata")
print(preenchido)

# Remover todos os elementos iguais a X
lista = [1, 2, 2, 3, 2, 4]
lista = [x for x in lista if x != 2]
print(lista)

