# Nome: Caio do Vale Soares
# Data: 13/11/2024
# Programa que lê N números e diz se é possível formar um polígono com eles

#quantidade de lados
n = int(input('Digite quantos lados o polígono vai ter: '))

#variáveis
lado = 1
maiorLado = 0
somaLados = 0

#leitura dos lados
for i in range(1,n+1):
    lado = int(input('Digite um lado: '))
    somaLados += lado
    if lado > maiorLado:
        maiorLado = lado

#resultado
if maiorLado > somaLados - maiorLado:
    print('Não foi possível formar um polígono com os lados digitados')
else:
    print('Você consegui formar um polígono com ', n, ' lados')