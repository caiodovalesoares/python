# Nome: Caio do Vale Soares
# Data: 02/11/2024
# Programa que calcula a soma dos primeiros N números inteiros ímpares, onde N é definido pelo usuário

N = int(input("Digite o valor de N: "))

#variáveis
soma = 0
cont = 0
num = 1

#soma dos N primeiros números ímpares
while cont < N:
    soma += num
    cont += 1
    num += 2

#resultado
print("A soma dos", N, "primeiros números ímpares é:", soma)
