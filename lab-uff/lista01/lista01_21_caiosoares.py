# Nome: Caio do Vale Soares
# Data: 13/11/2024
# Programa que calcula a somatória de 1 sobre i, onde i varia de 1 até N

som = 0

#valor de N
n = int(input('Digite o valor de N: '))

#somatória
for i in range(1,n+1):
    som += 1/i

#resultado
print('O valor da somatória é ', som)