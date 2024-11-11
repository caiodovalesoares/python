import random as r
r.seed()

conj = [r.randint(1,20) for _ in range (1, 11)]

print(conj)

soma = 0
maiorSoma = 0
for j in range(1, len(conj) - 1):
    soma = conj[j] + conj[j+1]
    if soma > maiorSoma:
        maiorSoma = soma
print(maiorSoma)