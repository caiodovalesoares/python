# Nome: Caio do Vale Soares
# Data: 02/11/2024
# Programa que analisa a altura de mulheres inscritas num concurso de beleza e depois escreve as duas maiores alturas e quantas mulheres as possuem

nome = str(input('Digite o nome da participante: '))
print('(MARIA encerra o programa)')

maiorAltura = 0
segMaiorAltura = 0
contMaior = 0
contSeg = 0
while nome != "MARIA" or nome != "maria":
    altura = float(input('Digite a altura da participante: '))
    if altura > maiorAltura:
        maiorAltura = altura
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

print('Maior altura: ', contMaior, 'mulheres com ', maiorAltura)
print('Segunda maior altura: ', contSeg, 'mulheres com ', segMaiorAltura)