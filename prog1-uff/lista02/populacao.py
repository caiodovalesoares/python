import math as m

populacaoA = int(input('Digite a população do país A: '))
populacaoB = int(input('Digite a população do país B: '))

contAno = 0
while populacaoA < populacaoB:
    populacaoA += (populacaoA/100)*3
    populacaoB += (populacaoB/100)*2
    contAno += 1

print(f'Demorariam {contAno} anos para o país A superar o país B')
print(f'O país A teria {m.ceil(populacaoA):,} habitantes e o país B teria {m.ceil(populacaoB):,} habitantes')