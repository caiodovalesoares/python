# Nome: Caio do Vale Soares
# Data: 11/12/24
# Programa que ordena um vetor sem usar sort()

import random

#criando vetor aleatório
vetor = [random.randint(0, 1000) for _ in range(100)]

#vetor desordenado
print("Vetor desordenado:")
print(vetor)

#algoritmo Bubble Sort
def bubble_sort(vetor):
    for i in range(len(vetor)):
        for j in range(len(vetor) - 1):
            if vetor[j] > vetor[j + 1]:
 #troca de elementos
                vetor[j], vetor[j + 1] = vetor[j + 1], vetor[j]
    return vetor

#ordenando o vetor
vetor_ordenado = bubble_sort(vetor)

#resultado
print("\nVetor ordenado:")
print(vetor_ordenado)