# Nome: Caio do Vale Soares
# Data: 01/11/2024
# Programa que calcula a soma de todos os números inteiros entre dois números A e B, excluindo A e B, desde que A seja menor ou igual a B.

#ler números inteiros A e B
A = int(input("Digite o número inteiro A: "))
B = int(input("Digite o número inteiro B: "))

#verificar se A é maior do que B
if A > B:
    print("A soma não será realizada, pois A é maior do que B.")
else:
    #calcular soma de números entre A e B
    soma = 0
    for i in range(A + 1, B):
        soma += i

    #exibir resultado
    print("A soma dos números entre A e B é:", soma)
