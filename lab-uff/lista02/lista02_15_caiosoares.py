# Nome: Caio do Vale Soares
# Data: 07/12/24
# Programa que lê um número e calcula o número correspondente na base decimal informada

#lendo os dados
numero = input('Digite o número: ')
base = int(input('Digite a base numérica (menor que 10): '))

decimal = 0
potencia = 0

#contando o número de dígitos
for i in numero:
    potencia += 1

#convertendo para decimal
potencia -= 1
for digito in numero:
    decimal += int(digito) * (base ** potencia)
    potencia -= 1

#resultado
print('O número decimal correspondente é:', decimal)