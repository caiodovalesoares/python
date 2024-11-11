a = int(input('Digite o primeiro número: '))
b = int(input('Digite o segundo número: '))
mult3 = []
mult5 = []
mult7 = []

if a < b:
    for i in range(a, b):
        if i % 3 == 0:
            mult3.append(i)
        if i % 5 == 0:
            mult5.append(i)
        if i % 7 == 0:
            mult7.append(i)
           
    print(f'Múltiplos de 3: {mult3}')
    print(f'Múltiplos de 5: {mult5}')
    print(f'Múltiplos de 7: {mult7}')
else:
    print('Números inválidos, o primeiro deve ser menor do que o segundo')