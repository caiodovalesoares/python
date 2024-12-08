# Nome: Caio do Vale Soares
# Data: 07/12/24
# Programa que preenche uma matriz com valores aleatórios e calcula seu determinante 

import random

#preenchendo matriz 3x3 com valores aleatórios
matriz = [[random.randint(1, 10) for _ in range(3)] for _ in range(3)]

#matriz
print("Matriz:")
for linha in matriz:
    print(linha)

#calculando determinante
det = matriz[0][0] * (matriz[1][1] * matriz[2][2] - matriz[1][2] * matriz[2][1]) - \
      matriz[0][1] * (matriz[1][0] * matriz[2][2] - matriz[1][2] * matriz[2][0]) + \
      matriz[0][2] * (matriz[1][0] * matriz[2][1] - matriz[1][1] * matriz[2][0])

#determinante
print("\nDeterminante:", det)