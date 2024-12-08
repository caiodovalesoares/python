# Nome: Caio do Vale Soares
# Data: 04/12/24
# Programa que condensa elementos em uma lista

#função que condensa a lista
def condensa(L):
    #ordenando a lista
    L.sort()
    #lista auxiliar
    aux = []
    cont = 1

    #usando a lista auxiliar para condensar a lista principal
    for i in range(1, len(L)):
        if L[i] == L[i-1]:
            cont += 1
        if L[i] != L[i-1] and cont == 1:
            aux.append(str(L[i-1]))
        if L[i] != L[i-1] and cont > 1:
            aux.append(str(f'{L[i-1]}^{cont}'))
            cont = 1

    #append do último termo da lista
    if cont > 1:
        aux.append(str(f'{L[i]}^{cont}'))
    else:
        aux.append(str(L[i]))

    #resultado da função
    L.clear()
    L.extend(aux)
    return L

#lendo as informações da lista
elementos = int(input('Digite a quantidade de itens da lista: '))
L = []
for j in range(elementos):
    L.append(int(input(f'Digite o {j+1}° item da lista: ')))

#resultado
print(f'Lista condensada: {condensa(L)}')