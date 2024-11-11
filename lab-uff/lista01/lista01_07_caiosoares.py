# Nome: Caio do Vale Soares
# Data: 02/11/2024
# Programa que lê dois números A e B e calcula todos os múltiplos de 4 entre eles

#lendo números inteiros A e B
A = int(input("Digite o número inteiro A: "))
B = int(input("Digite o número inteiro B: "))

#verificando se A é maior do que B
if A > B:
    print("A soma não será realizada, pois A é maior do que B.")
else:
    #iniciando a soma
    soma = 0
    
    #calculando soma de múltiplos de 4
    i = A + 1
    while i < B:
        if i % 4 == 0:
            soma += i
        i += 1
    
    #resultado
    print("A soma dos múltiplos de 4 entre A e B é: ", soma)
