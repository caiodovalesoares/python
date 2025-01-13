simbol = ''
with open('c:/Users/caiod/OneDrive/Documentos/estudos/python/prog1-uff/lista04/conta.txt', 'w') as archive:
    while simbol != '=':
        floatNumber = float(input('Digite um número real: '))
        archive.write(f'{floatNumber}\n')
        simbol = input('"+" para somar\n"-" para subtrair\n"*" para multiplicar\n"/" para dividir\n"=" para ver o resultado\nDigite um sinal: ')
        if simbol != '=':
            archive.write(f'{simbol}\n')