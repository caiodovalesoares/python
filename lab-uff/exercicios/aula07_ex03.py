frase = str(input('Digite uma frase: '))

frase = frase.lower()
print(frase)
contador = frase.count('a')

frase = frase.upper()
print(frase)

print(f'Quantidade de letras "a": {contador}')