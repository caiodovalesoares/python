string = str(input('Digite uma frase: '))
string = string.lower()

characters = {}

for i in range(len(string)):
    if string[i] not in characters:
        characters[f'{string[i]}'] = string.count(string[i])

print(characters)
print(f'Caracteres únicos: {len(characters)}')