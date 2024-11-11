n = int(input('Digite um número: '))
divisores = []
soma = 0

if n > 0:
    for i in range(1,n):
        if n % i == 0:
            divisores.append(i)
            soma += i
else:
    print('O valor digitado precisa ser positivo')
if soma == n:
    print(f'O número {n} é perfeito pois os seus divisores {divisores} somados resultam em {n}')
else:
    print(f'O número {n} não é perfeito pois os seus divisores {divisores} somados não resultam em {n}')