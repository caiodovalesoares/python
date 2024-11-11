# Nome: Caio do Vale Soares
# Data: 24/10/2024
# Programa que lê dois números e diz qual é o maior entre eles

num1 = int(input('Entre com o primeiro número: '))
num2 = int(input('Entre com o segundo número: '))
if num1 > num2:
    print('O primeiro número é o maior!')
elif num1 < num2:
    print('O segundo número é o maior!')
else: # Se nenhum for maior que o outro, significa que eles são iguais
    print('Os dois números são iguais!')