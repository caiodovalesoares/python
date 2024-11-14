# Nome: Caio do Vale Soares
# Data: 13/11/2024
# Programa que simula um saque num caixa eletrônico e diz quantas notas de cada valor vão ser entregues

#variáveis
nota50 = 0
nota20 = 0
nota10 = 0
nota5 = 0
nota1 = 0

saque = int(input('Digite o valor do saque:'))

#checando quantas notas de cada valor vão ser entregues
if saque>50:
    nota50 = saque // 50
    nota20 = (saque%50) // 20
    nota10 = ((saque%50)%20) // 10
    nota5 = (((saque%50)%20)%10) // 5
    nota1 = ((((saque%50)%20)%10)%5) // 1
elif saque < 50 and saque >= 20:
    nota20 = saque // 20
    nota10 = (saque%20) // 10
    nota5 = ((saque%20)%10) // 5
    nota1 = (((saque%20)%10)%5) // 1
elif saque < 20 and saque >= 10:
    nota10 = saque // 10
    nota5 = (saque%10) // 5
    nota1 = ((saque%10)%5) // 1
elif saque < 10 and saque >= 5:
    nota5 = saque // 5
    nota1 = (saque%5) // 1
elif saque < 5:
    nota1 = saque // 1

#resultado
if nota50 != 0:
    print(nota50, ' nota(s) de 50 reais')
if nota20 != 0:
    print(nota20, ' nota(s) de 20 reais')
if nota10 != 0:
    print(nota10, ' nota(s) de 10 reais')
if nota5 != 0:
    print(nota5, ' nota(s) de 5 reais')
if nota1 != 0:
    print(nota1, ' nota(s) de 1 real')