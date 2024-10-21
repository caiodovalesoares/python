saldo = float(input('Digite seu saldo:'))
match saldo:
    case saldo if saldo <= 200:
        print(f'O seu saldo é de {saldo} reais e você não está apto para receber o crédito.')
    case saldo if saldo > 200 and saldo < 401:
        print(f'O seu saldo é de {saldo} reais e você possui {saldo/5:.2f} reais de crédito.')
    case saldo if saldo > 400 and saldo < 601:
        print(f'O seu saldo é de {saldo} reais e você possui {(saldo/10)*3:.2f} reais de crédito.')
    case saldo if saldo > 600:
        print(f'O seu saldo é de {saldo} reais e você possui {(saldo/10)*4:.2f} reais de crédito.')