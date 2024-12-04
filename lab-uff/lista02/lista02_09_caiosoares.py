# Nome: Caio do Vale Soares
# Data: 02/12/24
# Programa que recebe uma matriz e retorna quantos elementos nela são maiores que 10

def mat_maior_10(matriz):
    for linha in matriz:
        print(linha)
    if cont10 > 0:
        return (f'Existem {cont10} elementos maiores que 10 nessa matriz')
    else:
        return ('Não existem elementos maiores que 10 nessa matriz')

linha = []
matriz = []

#tamanho da matriz
linhas = int(input("Digite o número de linhas: "))
colunas = int(input("Digite o número de colunas: "))

#contador de números maiores que 10
cont10 = 0

for i in range(linhas):
    linha = []
    for j in range(colunas):
        #lendo os elementos da matriz
        linha.append(int(input(f'Digite o elemento [{i+1}][{j+1}]: ')))
        #checando se o elemento é maior que 10
        if linha[j] > 10:
            cont10 += 1
    matriz.append(linha)

print('=-' * 30)

#resultado
print(mat_maior_10(matriz))