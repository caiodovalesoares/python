peso = float(input('Digite seu peso: '))
print('1) Mercúrio\n2) Vênus\n3) Marte\n4) Júpiter\n5) Saturno\n6) Urano')
planet = int(input('Selecione um planeta com um número de 1 a 6: '))

match planet:
    case 1:
        print(f'No planeta Mercúrio você pesaria {peso*0.37:.2f} kg')
    case 2:
        print(f'No planeta Vênus você pesaria {peso*0.88:.2f} kg')
    case 3:
        print(f'No planeta Marte você pesaria {peso*0.38:.2f} kg')
    case 4:
        print(f'No planeta Júpiter você pesaria {peso*2.64:.2f} kg')
    case 5:
        print(f'No planeta Saturno você pesaria {peso*1.15:.2f} kg')
    case 6:
        print(f'No planeta Urano você pesaria {peso*1.17:.2f} kg')
    case _:
        print('RESPOSTA INVÁLIDA')