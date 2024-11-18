# Nome: Caio do Vale Soares
# Data: 15/11/2024
# Programa que lê dois números A e B, calcula o MDC entre eles e a quantidade de divisores comuns entre eles

#números usados
A = int(input('Digite o primeiro número: '))
B = int(input('Digite o segundo número: '))

#variáveis
mdc = 0
contDivisores = 0

#checando os divisores
for i in range(2, A+1):
    if A % i == 0 and B % i == 0:
        contDivisores +=1
        if i > mdc:
            mdc = i

#resultando
print('Os números tem o total de ', contDivisores, ' divisores em comum e o MDC entre eles é: ', mdc)