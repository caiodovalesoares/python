dia = int(input('Digite um número entre 1 e 365:'))

if dia <= 31:
    print(f'Dia {dia} de Janeiro')

if dia > 31 and dia <= 59:
    dia = dia - 31
    print(f'Dia {dia} de Fevereiro')

if dia > 59 and dia <= 90:
    dia = dia - 59
    print(f'Dia {dia} de Março')

if dia > 90 and dia <= 120:
    dia = dia - 90
    print(f'Dia {dia} de Abril')

if dia > 120 and dia <= 151:
    dia = dia - 120
    print(f'Dia {dia} de Maio')

if dia > 151 and dia <= 181:
    dia = dia - 151
    print(f'Dia {dia} de Junho')

if dia > 181 and dia <= 212:
    dia - 181
    print(f'Dia {dia} de Julho')

if dia > 212 and dia <= 243:
    dia = dia - 212
    print(f'Dia {dia} de Agosto')

if dia > 243 and dia <= 273:
    dia = dia - 243
    print(f'Dia {dia} de Setembro')

if dia > 273 and dia <= 304:
    dia = dia - 273
    print(f'Dia {dia} de Outubro')

if dia > 303 and dia <= 334:
    dia = dia - 303
    print(f'Dia {dia} de Novembro')

if dia > 334 and dia <= 365:
    dia = dia - 334
    print(f'Dia {dia} de Dezembro')