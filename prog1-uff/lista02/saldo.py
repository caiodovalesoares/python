saldo = float(input('Digite o saldo da sua conta: '))
mes = int(input('Digite quantos meses você vai deixar o dinheiro no banco: '))
saldoFinal = 0

if mes < 12:
    saldoFinal = saldo
    for i in range(1, mes + 1):
        saldoFinal += (saldo/200)
    print(f'Saldo da conta após {mes} meses: {saldoFinal}')

if mes >= 12:
    if saldo >= 20000:
        saldoFinal = saldo
        for i in range(1, mes + 1):
            saldoFinal += (saldo/200)
            if i % 12 == 0:
                saldoFinal += saldo/100
        print(f'Saldo da conta após {mes} meses: {saldoFinal}')
    if saldo < 20000 and saldo >= 10000:
        saldoFinal = saldo
        for i in range(1, mes + 1):
            saldoFinal += (saldo/200)
            if i % 12 == 0:
                saldoFinal += saldo/200
        print(f'Saldo da conta após {mes} meses: {saldoFinal}')