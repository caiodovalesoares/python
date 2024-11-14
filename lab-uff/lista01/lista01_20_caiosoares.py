# Nome: Caio do Vale Soares
# Data: 13/11/2024
# Programa que imprime os 4 primeiros números perfeitos

#variáveis
contPerfeito = 0
n = 2

while contPerfeito < 4:
    soma = 0
    for i in range(1,n):
        #encontrando os divisores do número e os somando
        if n % i == 0:
            soma += i
    #comandos quando o programa acha um número perfeito
    if soma == n:
        contPerfeito += 1
        print(n)
    n += 1