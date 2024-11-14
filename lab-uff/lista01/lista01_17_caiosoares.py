# Nome: Caio do Vale Soares
# Data: 13/11/2024
#Programa que verifica se um número é primo

#variável
contDivisor = 0
n = int(input('Digite o número: '))

#checando se o número é primo
for i in range(2,n):
    if n % i == 0:
        contDivisor += 1

#resultado
if contDivisor > 0:
    print('O número não é primo')
else:
    print('O número é primo')