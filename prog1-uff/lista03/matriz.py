linhas = int(input('Digite a quantidade de linhas: '))
colunas = int(input('Digite a quantidade de colunas: '))

matriz = []
for i in range(linhas):
    matriz.append([])
    for j in range(colunas):
        valor = int(input(f'Digite o valor da linha {i+1}, coluna {j+1}: '))
        matriz[i].append(valor)

for i in range(linhas):
    for j in range(colunas):
        print(f'[{matriz[i][j]:^5}]', end='')
    print()