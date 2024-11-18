# Nome: Caio do Vale Soares
# Data: 15/11/2024
# Programa que lê coeficientes A, B, C e D e verificar se existe a ocorrência de uma raiz

#lendo os coeficientes
A = float(input('Digite o coeficiente A: '))
B = float(input('Digite o coeficiente B: '))
C = float(input('Digite o coeficiente C: '))
D = float(input('Digite o coeficiente D: '))

#variáveis
intervaloInicial = -1000
intervaloFinal = 1000
passo = 0.001

x = intervaloInicial
anterior = A*x**3 + B*x**2 + C*x + D

while x <= intervaloFinal:
    x += passo
    atual = A*x**3 + B*x**2 + C*x + D
    
    #verificando se há raiz
    if atual * anterior < 0:
         print('Existe raiz no intervalo [' + str(x - passo) + ', ' + str(x) + ']')
    
    anterior = atual
