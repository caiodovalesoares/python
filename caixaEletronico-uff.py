nota50 = 0
nota10 = 0
nota5 = 0
nota1 = 0

saque = int(input('Digite o valor do saque:'))
if saque>50:
    nota50 = saque // 50
    nota10 = (saque%50) // 10
    nota5 = ((saque%50)%10) // 5
    nota1 = (((saque%50)%10)%5) // 1
elif saque < 50 and saque >= 10:
    nota10 = saque // 10
    nota5 = (saque%10) // 5
    nota1 = ((saque%10)%5) // 1
elif saque < 10 and saque >= 5:
    nota5 = saque // 5
    nota1 = (saque%5) // 1
elif saque < 5:
    nota1 = saque // 1

if nota50 != 0:
    print(f'{nota50} nota(s) de 50 reais')
if nota10 != 0:
    print(f'{nota10} nota(s) de 10 reais')
if nota5 != 0:
    print(f'{nota5} nota(s) de 5 reais')
if nota1 != 0:
    print(f'{nota1} nota(s) de 1 real')