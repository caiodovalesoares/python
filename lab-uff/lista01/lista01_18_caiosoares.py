# Nome: Caio do Vale Soares
# Data: 13/11/2024
# Programa que imprime os N primeiros números primos

#quantidade de primos
n = int(input('Digite a quantidade de primos desejada: '))

#variáveis
primos = 0
num = 2

#verificando se o número é primo
while primos < n:
    contDiv = 0
    for i in range(2, num):
        if num % i == 0:
            contDiv += 1
    if contDiv == 0:
        print(num)
        primos += 1
    num += 1