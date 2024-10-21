print('--------------------------')
print('CONVERSOR DE MILISSEGUNDOS')
print('--------------------------')
ms = int(input('Digite o tempo em milissegundos: '))
segs = ms//1000
mins = segs//60
horas = mins//60
minutos = mins%60
segundos = segs%60

match horas:
    case 1:
        print(f'{horas} hora')
    case horas if horas > 1:
        print(f'{horas} horas')

match minutos:
    case 1:
        print(f'{minutos} minuto')
    case minutos if minutos > 1:
        print(f'{minutos} minutos')

match segundos:
    case 1:
        print(f'{segundos} segundo')
    case segundos if segundos > 1:
        print(f'{segundos} segundos')