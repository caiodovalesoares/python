lista = []

resp = ''
while resp != 'f':
    print('(A) para adicionar um elemento na lista.\n(R) para remover elemento da lista.\n(I) para imprimir a lista.\n(F) para sair.')

    resp = str(input('O que você deseja fazer? '))
    resp = resp.lower()

    match resp:
        case 'a':
            num = int(input('Digite o número:'))
            lista.append(num)
        case 'r':
            num = int(input('Digite o número:'))
            if num in lista:
                lista.remove(num)
        case 'i':
            print(lista)

print(f'Lista: {lista}')