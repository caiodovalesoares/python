# Nome: Caio do Vale Soares
# Data: 15/11/2024
# Programa que calcula os dias existentes entre duas datas

#data do primeiro dia
D1 = int(input('Digite o dia da primeira data: '))
M1 = int(input('Digite o mês da primeira data: '))
A1 = int(input('Digite o ano da primeira data: '))

#data do segundo dia
D2 = int(input('Digite o dia da segunda data: '))
M2 = int(input('Digite o mês da segunda data: '))
A2 = int(input('Digite o ano da segunda data: '))

#variáveis
total_dias1 = 0
total_dias2 = 0
ano = 1

while ano < A1:
    #checando se o ano é bissexto
    if ano % 4 == 0 and (ano % 100 != 0 or ano % 400 == 0):
        total_dias1 += 366
    else:
        total_dias1 += 365
    ano += 1

mes = 1
while mes <= M1 - 1:
    #checando quantos dias tem o mês
    if mes == 2:
        if A1 % 4 == 0 and (A1 % 100 != 0 or A1 % 400 == 0):
            total_dias1 += 29
        else:
            total_dias1 += 28
    elif mes == 4 or mes == 6 or mes == 9 or mes == 11:
        total_dias1 += 30
    else:
        total_dias1 += 31
    mes += 1

total_dias1 += D1

ano = 1
while ano < A2:
    #checando se o ano é bissexto
    if ano % 4 == 0 and (ano % 100 != 0 or ano % 400 == 0):
        total_dias2 += 366
    else:
        total_dias2 += 365
    ano += 1

mes = 1
while mes <= M2 - 1:
    #checando quantos dias tem o mês
    if mes == 2:
        if A2 % 4 == 0 and (A2 % 100 != 0 or A2 % 400 == 0):
            total_dias2 += 29
        else:
            total_dias2 += 28
    elif mes == 4 or mes == 6 or mes == 9 or mes == 11:
        total_dias2 += 30
    else:
        total_dias2 += 31
    mes += 1

total_dias2 += D2

#calculando a diferença de dias
diferenca_dias = 0
if total_dias2 > total_dias1:
    diferenca_dias = total_dias2 - total_dias1
else:
    diferenca_dias = total_dias1 - total_dias2

#resultado
print("A diferenca entre as datas é de ")
print(diferenca_dias)
print("dias.")