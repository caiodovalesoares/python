# Nome: Caio do Vale Soares
# Data: 04/12/24
# Programa que cria uma função que multiplica duas matrizes

#função que multiplica as matrizes
def multiplica_matriz(mat1, mat2):
    if len(mat1[0]) != len(mat2):
        return 'Matrizes não são compatíveis para multiplicação'

    mat3 = [[0 for _ in range(len(mat2[0]))] for _ in range(len(mat1))]

    for i in range(len(mat1)):
        for j in range(len(mat2[0])):
            for k in range(len(mat2)):
                mat3[i][j] += mat1[i][k] * mat2[k][j]

    return mat3

#quantidade de linhas e colunas das matrizes
linhas1 = int(input('Digite o número de linhas da primeira matriz: '))
colunas1 = int(input('Digite o número de colunas da primeira matriz: '))
linhas2 = int(input('Digite o número de linhas da segunda matriz: '))
colunas2 = int(input('Digite o número de colunas da segunda matriz: '))

#mensagem de erro
if colunas1 != linhas2:
    print('Matrizes não são compatíveis para multiplicação')
else:
    mat1 = []
    for i in range(linhas1):
        linha1 = []
        for j in range(colunas1):
            linha1.append(int(input(f'Digite o elemento [{i+1}][{j+1}] da primeira matriz: ')))
        mat1.append(linha1)

    mat2 = []
    for i in range(linhas2):
        linha2 = []
        for j in range(colunas2):
            linha2.append(int(input(f'Digite o elemento [{i+1}][{j+1}] da segunda matriz: ')))
        mat2.append(linha2)

    #matriz 1
    print('Matriz 1:')
    for linha in mat1:
        print(linha)
    #matriz 2
    print('Matriz 2:')
    for linha in mat2:
        print(linha)
    #resultado
    print('Matriz resultante:')
    for linha in multiplica_matriz(mat1, mat2):
        print(linha)