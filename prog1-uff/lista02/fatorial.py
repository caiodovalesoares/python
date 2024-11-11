fat = 1
num = int(input('Digite um número: '))
n = num
for n in range(n, 1, -1):
    fat = fat * n

print(f'Fatorial de {num} ({num}!): {fat}')
    