# Nome: Caio do Vale Soares
# Data: 26/11/24
# Programa que lê 50 valores de temperaturas em graus Celsius e as transforma em Farenheit, depois imprime a média em Celsius e Farenheit e diz quantas temperaturas ficaram acima da média em Farenheit

#listas
totalC = []
totalF = []
maioresMedia = []

#lendo as temperaturas
for i in range(50):
    celsius = float(input('Digite a temperatura em graus Celsius: '))
    totalC.append(celsius)
    #transformando Celsius em Farenheit
    totalF.append((celsius*1.8) + 32)

#média em Celsius
mediaC = sum(totalC) / 50
print(f'Média em graus Celsius: {mediaC:.2f}')

#média em Farenheit
mediaF = sum(totalF) / 50
print(f'Média em graus Farenheit: {mediaF:.2f}')

for j in range(50):
    if totalF[j] > mediaF:
        maioresMedia.append(f'{totalF[j]:.2f}')

#valores acima da média
print(f'Valores em Farenheit acima da média: {maioresMedia}')