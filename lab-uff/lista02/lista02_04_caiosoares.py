# Nome: Caio do Vale Soares
# Data: 26/11/24
# Programa que lê uma lista de 30 números e depois conta quantas vezes um número x apareceu nela

#criando a lista
lista = []

#lendo os números
for i in range(30):
    lista.append(int(input('Digite um número: ')))

#perguntando o valor de x
x = int(input('Digite o número que você deseja contar: '))

#resultado
print(f'Esse número apareceu {lista.count(x)} vezes')