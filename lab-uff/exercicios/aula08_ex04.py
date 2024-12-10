import math as m

turma1 = [1.1, 7.5, 0.8, 1.8, 1.5, 1.9, 10.0, 10.0, 9.3, 10.0, 7.7, 0.6, 0.5, 8.7, 5.6, 7.0, 8.3, 7.0, 9.1, 7.4, 8.1, 7.0, 6.3, 0.6, 7.4, 2.8, 5.0, 1.4, 1.5, 0.5, 8.3, 7.0, 2.9, 7.6, 10.0, 3.3, 1.9, 5.1, 7.0]

media1 =sum(turma1)/len(turma1)

print(f'Maior nota da turma 1: {max(turma1)}')
print(f'Menor nota da turma 1: {min(turma1)}')
print(f'Média da turma 1: {media1:.2f}')

desvio1 = 0
for i in range(len(turma1)):
    n = (turma1[i]-media1) ** 2
    desvio1 += n
desvio1 = m.sqrt(desvio1/len(turma1))
print(f'Desvio padrão da turma 1: {desvio1:.2f}')

turma2 = [10.0, 8.2, 8.7, 5.5, 6.8, 8.6, 8.5, 6.1, 6.2, 8.5, 7.7, 10.0, 10.0, 6.1, 8.4, 5.4, 5.6, 9.8, 2.1, 8.5, 3.3, 8.7, 8.5, 9.1, 9.7]

media2 = sum(turma2)/len(turma2)

print(f'Maior nota da turma 2: {max(turma2)}')
print(f'Menor nota da turma 2: {min(turma2)}')
print(f'Média da turma 2: {media2:.2f}')

desvio2 = 0
for i in range(len(turma2)):
    n = (turma2[i]-media2) ** 2
    desvio2 += n
desvio2 = m.sqrt(desvio2/len(turma2))
print(f'Desvio padrão da turma 2: {desvio2:.2f}')