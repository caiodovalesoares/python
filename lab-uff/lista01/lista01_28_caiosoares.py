# Nome: Caio do Vale Soares
# Data: 15/11/2024
# Programa que lê um número decimal e o converte para base hexadecimal

numero = int(input('Digite o número decimal: '))

#variáveis
hexadecimal = ''
hexDigitos = '0123456789ABCDEF'

#convertendo para hexadecimal
while numero > 0:
    resto = numero % 16
    hexadecimal = hexDigitos[resto] + hexadecimal
    numero //= 16

#resultado
print('O número hexadecimal correspondente é:', hexadecimal)
