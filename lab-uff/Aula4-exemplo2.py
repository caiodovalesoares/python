# Nome: Caio do Vale Soares
# Data: 24/10/2024
# Programa que lê um número e diz se ele é par ou ímpar

num = int(input('Entre com um número: '))
if num % 2 == 1: # Se o resto da divisão do número por 2 for igual a 1, significa que ele é ímpar
    print('O número é impar!')
else: # Caso contrário, ele é par
    print('O número é par!')