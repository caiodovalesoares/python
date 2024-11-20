lista = []
for i in range(1,999):
    num = int(input('Digite um número: '))
    lista.append(num)
    if i % 5 == 0:
        print(lista)
        lista.clear()
    if num == 0:
        print(lista)
        break