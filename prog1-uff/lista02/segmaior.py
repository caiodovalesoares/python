i = 1
maior = 0
segMaior = 0
for i in range(i,11):
    num = int(input('Digite um número: '))
    if num > maior:
        segMaior = maior
        maior = num
    if num < maior and num > segMaior:
        segMaior = num

print(f'O segundo maior valor é {segMaior}')