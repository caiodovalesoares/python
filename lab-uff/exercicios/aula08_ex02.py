lista1 = []
lista2 = []
lista3 = []

num = 0
while num != -1:
    num = (int(input('Digite um valor para a primeira lista (-1 encerra a leitura): ')))
    lista1.append(num)

num = 0
while num != -1:
    num = (int(input('Digite um valor para a segunda lista (-1 encerra a leitura): ')))
    lista2.append(num)

lista1.remove(-1)
lista2.remove(-1)
print(f'Lista 1: {lista1}')
print(f'Lista 2: {lista2}')

for i in range(len(lista1)):
    if lista1[i] in lista2:
        lista2.remove(lista1[i])
        lista3.append(lista1[i])

lista3.sort()
print(f'Interseção Lista 1 e Lista 2: {lista3}')