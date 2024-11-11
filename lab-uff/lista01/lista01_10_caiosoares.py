# Nome: Caio do Vale Soares
# Data: 02/11/2024
# Programa que calcula a soma dos 20 primeiros números pares

#variáveis
soma = 0
cont = 0
num = 2

#soma dos primeiros 20 números pares
while cont < 20:
    soma += num
    cont += 1
    num += 2

#resultado
print("A soma dos primeiros 20 números pares é:", soma)
