seq = str(input('Digite a sequência de letras: '))

cont = 1
for i in range(1, len(seq)):
    if seq[i] == seq[i-1]:
        cont += 1
    else:
        print(f'{seq[i-1]}{cont}')
        cont = 1
print(f'{seq[i]}{cont}')