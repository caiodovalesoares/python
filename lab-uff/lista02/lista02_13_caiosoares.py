# Nome: Caio do Vale Soares
# Data: 04/12/24
# Programa que mostra os primeiros N números primos

#função que checa os números primos e devolve a quantidade desejada
def primos(n):
    conjPrimos = []

    #variáveis
    num = 2
    primos = 0

    while primos < n:
        contDiv = 0
        for i in range(2, num):
            if num % i == 0:
                contDiv += 1
        if contDiv == 0:
            conjPrimos.append(num)
            primos += 1
        num += 1
    return conjPrimos

#quantidade de primos desejada
n = int(input('Digite a quantidade de primos desejada: '))

#resultado
print(primos(n))