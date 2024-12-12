# Nome: Caio do Vale Soares
# Data: 11/12/24
# Programa que decompõe (num) em fatores primos

#função que faz a decomposição
def fat_primo(num):
    fatores = []
    divisor = 2

    while num > 1:
        potencia = 0
        while num % divisor == 0:
            num //= divisor
            potencia += 1
        if potencia > 0:
            fatores.append(f"{divisor}^{potencia}")
        divisor += 1

    return fatores

#lendo o valor de num
num = int(input('Digite o número: '))
#resultado
print(fat_primo(num))