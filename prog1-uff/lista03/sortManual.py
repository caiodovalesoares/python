a = []
b = []
c = []
tamanhoA = int(input('Digite quantos números vai possuir a lista A: '))
tamanhoB = int(input('Digite quantos números vai possuir a lista B: '))
print('-='*30)

for i in range(0,tamanhoA):
    a.append(int(input(f'Digite o {i+1}° elemento da lista A: ')))
for i in range(0,tamanhoB):
    b.append(int(input(f'Digite o {i+1}° elemento da lista B: ')))
print('-='*30)

i = 0
j = 0
while i < len(a) and j < len(b):
    if a[i] <= b[j]:
        c.append(a[i])
        i += 1
    else:
        c.append(b[j])
        j += 1

c.extend(a[i:])
c.extend(b[j:])

print(c)