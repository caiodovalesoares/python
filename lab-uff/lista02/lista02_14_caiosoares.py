# Nome: Caio do Vale Soares
# Data: 04/12/24
# Programa que simula um saque num caixa eletrônico e diz quantas notas de cada valor vão ser entregues

#variáveis
nota100 = 0
nota50 = 0
nota20 = 0
nota10 = 0
nota5 = 0
nota1 = 0

saque = int(input('Digite o valor do saque: '))

#checando quantas notas de cada valor vão ser entregues
while saque >= 100:
    saque -= 100
    nota100 += 1
    if nota100 == 10:
        break

while saque >= 50:
    saque -= 50
    nota50 += 1
    if nota50 == 10:
        break

while saque >= 20:
    saque -= 20
    nota20 += 1
    if nota20 == 10:
        break

while saque >= 10:
    saque -= 10
    nota10 += 1
    if nota10 == 10:
        break

while saque >= 5:
    saque -= 5
    nota5 += 1
    if nota5 == 10:
        break

while saque >= 1:
    saque -= 1
    nota1 += 1
    if nota1 == 10:
        break

#resultado
if saque == 0:
    if nota100 != 0:
        print(nota100, ' nota(s) de 100 reais')
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
        
#mensagem de erro
else:
    print('Não foi possível realizar o saque!\nQuantidade de notas insuficiente')