# Nome: Caio do Vale Soares
# Data: 13/11/2024
# Programa que verigfica se um número é perfeito

n = int(input('Digite um número: '))
soma = 0

#o número precisa ser positivo
if n > 0:
    for i in range(1,n):
        #encontrando os divisores do número e os somando
        if n % i == 0:
            soma += i
else:
    print('O valor digitado precisa ser positivo')
#resultado
if soma == n:
    print('O número ', n, ' é perfeito')
else:
    print('O número ', n, ' não é perfeito')