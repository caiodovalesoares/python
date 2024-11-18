# Nome: Caio do Vale Soares
# Data: 15/11/2024
# Programa que fatora um número N inteiro

#número desejado
n = int(input('Digite o número: '))
contDiv = 0

#verificando os divisores
while n != 1:
    for i in range(2,n+1):
        while n % i == 0:
            n = n // i
            contDiv += 1
        #resultado
        if contDiv > 0:
            print(i, '^', contDiv)
        contDiv = 0