# Nome: Caio do Vale Soares
# Data: 26/11/24
# Programa que lê 40 números e informa quantos são pares

lista = []
contPar = 0
for i in range(40):
    lista.append(int(input('Digite um número: ')))
    if lista[i] % 2 == 0:
        contPar +=1

print(f'Existem {contPar} números pares nessa lista!')