n = int(input('Digite a quantidade de alunos: '))

acimaMedia = []
notas = []

for i in range(n):
    nota = float(input(f'Digite a nota do {i+1}° aluno: '))
    notas.append(nota)

media = sum(notas) / n

for i in range(n):
    if notas[i] > media:
        acimaMedia.append(notas[i])

print(f'Notas dos alunos: {notas}')
print(f'Média da turma: {media}')
print(f'Quantidade de alunos acima da média: {len(acimaMedia)}')