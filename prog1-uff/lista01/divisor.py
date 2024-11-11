n1 = float(input('Digite o primeiro número: '))
n2 = float(input('Digite o segundo número: '))
n3 = float(input('Digite o terceiro número: '))

if n1>=n2:
    div = n1 / n2
    print(f'{n1}/{n2} = {div}')
if n1>=n3 and n3!=n2:
    div = n1 / n3
    print(f'{n1}/{n3} = {div}')
if n2>n1:
    div = n2 / n1
    print(f'{n2}/{n1} = {div}')
if n2>=n3 and n3!=n1:
    div = n2 / n3
    print(f'{n2}/{n3} = {div}')
if n3>n1:
    div = n3 / n1
    print(f'{n3}/{n1} = {div}')
if n3>n2 and n2!=n1:
    div = n3 / n2
    print(f'{n3}/{n2} = {div}')