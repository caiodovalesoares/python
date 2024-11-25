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
while len(c) != (len(a)+len(b)+2):
    if i == len(a):
        while a[i] > b[j]:    
            c.append(b[j])
            b.pop(j)
            j += 1
        else:
            c.append(a[i])
            c.extend(b)
            print(c)
            break
    if i == len(b):
        while b[j] > a[i]:    
            c.append(a[i])
            a.pop(i)
            i += 1
        else:
            c.append(b[j])
            c.extend(a)
            print(c)
            break
    if a[i] > b[j]:
        c.append(b[j])
        b.pop(j)
        j += 1
    if a[i] == b[j]:
        c.append(a[i])
        c.append(b[j])
        a.pop(i)
        b.pop(j)
        i += 1
        j += 1
    if a[i] < b[j]:
        c.append(a[i])
        a.pop(i)
        i += 1