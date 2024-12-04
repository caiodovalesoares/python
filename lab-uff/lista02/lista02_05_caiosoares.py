# Nome: Caio do Vale Soares
# Data: 26/11/24
# Programa que inverte os 8 primeiros números com os 8 últimos numa lista de 16 posições

#listas
lista = []
listaAux = []

for i in range(16):
    lista.append(int(input('Digite um número: ')))

#invertendo a lista original
listaAux.extend(lista[8:])
listaAux.extend(lista[0:8])

#lista original
print(lista)

#lista invertida
lista = listaAux
print(lista)