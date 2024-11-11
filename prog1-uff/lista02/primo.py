n = int(input('Digite um número: '))

while n < 1:
    print('Número inválido, digite um número positivo maior que dois.')
    n = int(input('Digite um número: '))

mult = 0
for i in range(2, n):
    if n % i == 0:
        mult += 1
if mult == 0:
    print(f'O número {n} é primo')
else:
    print(f'O número {n} não é primo')