a = int(input('Digite o primeiro número: '))
b = int(input('Digite o segundo número: '))
primos = []
mult = 0
if a < b and a > 0:
    for i in range(a, b):
        for j in range(2, i):
            if i % j == 0:
                mult += 1
        if mult == 0 and i != 1:
            primos.append(i)
        else:
            mult = 0

    print(f'Números primos: {primos}')
    if len(primos) == 0:
        print('Não há números primos')
else:
    print('Números inválidos, o primeiro deve ser menor do que o segundo')