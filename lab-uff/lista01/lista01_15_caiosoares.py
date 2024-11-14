# Nome: Caio do Vale Soares
# Data: 02/11/2024
# Programa que analisa a altura de mulheres inscritas num concurso de beleza e depois escreve as duas maiores alturas e quantas mulheres as possuem

nome = str(input('Digite o nome da participante: '))
print('(MARIA encerra o programa)')

#variáveis
maiorAltura = 0
segMaiorAltura = 0
contMaior = 0
contSeg = 0

#while para encerrar programa caso digitem maria
while nome != "MARIA" and nome != "maria":
    altura = float(input('Digite a altura da participante: '))
    #atribuição da segunda maior altura
    if altura > maiorAltura:
        segMaiorAltura = maiorAltura
        maiorAltura = altura
        contSeg = contMaior
        contMaior = 0
    if altura < maiorAltura and altura > segMaiorAltura:
        segMaiorAltura = altura
    if altura == maiorAltura:
        contMaior += 1
    if altura == segMaiorAltura:
        contSeg += 1
    nome = str(input('Digite o nome da participante: '))
    print('(MARIA encerra o programa)')
else:
    altura = float(input('Digite a altura da participante: '))
    if altura > maiorAltura:
        maiorAltura = altura
    if altura < maiorAltura and altura > segMaiorAltura:
        segMaiorAltura = altura
    if altura == maiorAltura:
        contMaior += 1
    if altura == segMaiorAltura:
        contSeg += 1

#resultado
if contMaior > 1:
    print('Maior altura: ', contMaior, 'mulheres com ', (maiorAltura), ' de altura')
else:
    print('Maior altura: ', contMaior, 'mulher com ', (maiorAltura), ' de altura')
if contSeg > 1:
    print('Segunda maior altura: ', contSeg, 'mulheres com ', segMaiorAltura, ' de altura')
else:
    print('Segunda maior altura: ', contSeg, 'mulher com ', segMaiorAltura, ' de altura')