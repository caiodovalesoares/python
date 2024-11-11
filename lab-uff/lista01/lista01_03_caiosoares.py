# Nome: Caio do Vale Soares
# Data: 01/11/2024
# Programa que lê números inteiros e escreve a quantidade de pares e ímpares, além de calcular a média dos pares

contPar = 0
pares = 0
contImpar = 0
num = int(input('Digite um número: '))
while num != 0: #o programa para de ler os números caso o número 0 seja digitado
    if num % 2 == 0:
        contPar += 1
        pares += num
    else:
        contImpar += 1
    num = int(input('Digite um número: '))

mediaPares = pares / contPar #aqui eu calculei a média dos pares

print('O programa leu', contPar, 'números pares e', contImpar, 'Ímpares')
print('A média dos números pares é', mediaPares)