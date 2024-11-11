import sys

print('RESTAURANTE UNIVERSITÁRIO UFF')
print('-----------------------------')
print('1) Vegetariano\n2) Peixe\n3) Frango\n4) Carne')
prato = int(input('Selecione seu prato principal usando números de 1 a 4: '))
match prato:
    case 1:
        cal = 180
    case 2:
        cal = 230
    case 3:
        cal = 250
    case 4:
        cal = 350
    case _:
        print('RESPOSTA INVÁLIDA')
        prato = int(input('Selecione seu prato principal usando números de 1 a 4: '))
        match prato:
            case 1:
                cal = 180
            case 2:
                cal = 230
            case 3:
                cal = 250
            case 4:
                cal = 350
            case _:
                print('RESPOSTA INVÁLIDA NOVAMENTE. TENTE DE NOVO')
                exit()

print('1) Abacaxi\n2) Sorvete diet\n3) Mousse diet\n4) Mousse de chocolate')
sobremesa = int(input('Selecione sua sobremesa usando números de 1 a 4: '))
match sobremesa:
    case 1:
        cal = cal + 75
    case 2:
        cal = cal + 110
    case 3:
        cal = cal + 170
    case 4:
        cal = cal + 200
    case _:
        print('RESPOSTA INVÁLIDA')
        sobremesa = int(input('Selecione sua sobremesa usando números de 1 a 4: '))
        match sobremesa:
            case 1:
                cal = cal + 75
            case 2:
                cal = cal + 110
            case 3:
                cal = cal + 170
            case 4:
                cal = cal + 200
            case _:
                print('RESPOSTA INVÁLIDA NOVAMENTE. TENTE DE NOVO')
                exit()

print('1) Chá\n2) Suco de laranja\n3) Suco de melão\n4) Refrigerante diet')
bebida = int(input('Selecione sua bebida usando números de 1 a 4: '))
match bebida:
    case 1:
        cal = cal + 20
    case 2:
        cal = cal + 70
    case 3:
        cal = cal + 100
    case 4:
        cal = cal + 65
    case _:
        print('RESPOSTA INVÁLIDA')
        bebida = int(input('Selecione sua bebida usando números de 1 a 4: '))
        match bebida:
            case 1:
                cal = cal + 20
            case 2:
                cal = cal + 70
            case 3:
                cal = cal + 100
            case 4:
                cal = cal + 65
            case _:
                print('RESPOSTA INVÁLIDA NOVAMENTE. TENTE DE NOVO')
                exit()
        
print(f'Sua refeição possui o total de {cal} calorias!')