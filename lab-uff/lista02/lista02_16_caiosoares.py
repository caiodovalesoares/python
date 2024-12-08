# Nome: Caio do Vale Soares
# Data: 07/12/24
# Programa que lê um número decimal e o converte para hexadecimal

#função que converte para hexadecimal
def decimal_para_hexadecimal(n):
    return hex(n)[2:].upper()

#resultado
numero_decimal = int(input("Digite um número decimal: "))
print(decimal_para_hexadecimal(numero_decimal))