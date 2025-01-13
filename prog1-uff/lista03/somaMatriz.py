import random as r

def matrixSum(matrix1, matrix2):
    matrix3 = []
    for i in range(5):
        matrix3.append([])
        for j in range(4):
            matrix3[i].append(matrix1[i][j] + matrix2[i][j])
    return matrix3

matrix1 = []
for i in range(5):
    matrix1.append([])
    for j in range(4):
        matrix1[i].append(r.randint(1,10))

for i in range(5):
    for j in range(4):
        print(f'[{matrix1[i][j]:^5}]', end='')
    print()

print('=-' * 30)

matrix2 = []
for i in range(5):
    matrix2.append([])
    for j in range(4):
        matrix2[i].append(r.randint(1,10))

for i in range(5):
    for j in range(4):
        print(f'[{matrix2[i][j]:^5}]', end='')
    print()

print('=-' * 30)

for i in range(5):
    for j in range(4):
        print(f'[{matrixSum(matrix1, matrix2)[i][j]:^5}]', end='')
    print()