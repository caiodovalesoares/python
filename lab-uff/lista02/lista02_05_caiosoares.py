# Nome: Caio do Vale Soares
# Data: 26/11/24
# Programa que inverte uma lista de 16 posições

#listas
lista = []
lista2 = []

for i in range(16):
    lista.append(int(input('Digite um número: ')))

#invertendo a lista original
lista2.extend(lista[8:])
lista2.extend(lista[0:8])

#resultado
print(lista)
print(lista2)