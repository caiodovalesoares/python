def ascendent(numbers):
    numbers.sort()
    return numbers

numbers = []
length = int(input('Quantos números vai ter a lista: '))
for i in range(length):
    numbers.append(int(input(f'Digite o {i+1}° número: ')))

print(f'Lista ordenada: {ascendent(numbers)}')