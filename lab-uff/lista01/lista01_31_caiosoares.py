# Nome: Caio do Vale Soares
# Data: 15/11/2024
# Programa que calcula a raiz inteira de um número

n = int(input('Digite o número: '))

#variáveis
raiz = 0
raizInteira = 1

#calculando a raiz
while raiz <= n:
    raizInteira +=1
    raiz = raizInteira**2

#resultado
raizInteira -= 1
print('Raiz inteira de', n, ':', raizInteira)