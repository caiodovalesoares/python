# Nome: Caio do Vale Soares
# Data: 01/11/2024
# Programa que gera uma progressão aritmética (PA)

#aqui eu coletei as informações necessárias
primeiroTermo = int(input('Digite o primeiro termo da PA: '))
razao = int(input('Digite a razão da PA: '))
termos = int(input('Digite quantos termos você quer exibir: '))

for termos in range (1, termos+1): #usei esse for para limitar o número de termos exibidos
    print(primeiroTermo)
    primeiroTermo += razao