frutas = ["laranja","maça","uva"]
print(frutas)

frutas = []
print(frutas)

letras = list("python")
print(letras)

numeros = list(range(10))
print(numeros)

carro = ["Ferrari", "F8", 420000, 2020, 2900, "São Paulo", True]
print(carro)

#Listas alinhadas
matriz = [
    [1,"a", 2],
    ["b", 3, 4],
    [6, 5, "c"]
]

print(matriz[0])

#Fatiamento

lista = ['p','y', 't', 'h', 'o', 'n']
print(lista[2:])
print(lista[:2])
print(lista[0:3:2])

#Iterar lista

carros = ["gol", "celta", "palio"]

for carro in carros:
    print(carro)

#Enumarate

automovel = ["gol", "celta", "palio"]

for indice, carro in enumerate(automovel):
    print(f'{indice}: {carro}')

#Compreensão de listas

num = [1, 30, 21, 2, 9, 65, 34]
pares = []

for numeros in num:
    if numeros % 2 == 0:
        pares.append(numeros)

print(pares)