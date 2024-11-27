# Nome: Caio do Vale Soares
# Data: 26/11/24
# Programa que lê uma frase e imprime o total de vogais, o total de espaços e o resto

import unicodedata

contVogais = 0
contEspaco = 0
frase = str(input('Digite uma frase: '))

#passando a frase para minúsculas e tirando os caracteres especiais
frase = frase.lower()
frase = unicodedata.normalize('NFKD', frase).encode('ASCII', 'ignore').decode('ASCII')

for i in range(0, len(frase)):
    #checando se a sub-string é uma vogal
    if frase[i] == 'a' or frase[i] == 'e' or frase[i] == 'i' or frase[i] == 'o' or frase[i] == 'u':
        contVogais += 1
    #checando se a sub-string é um espaço
    if frase[i] == ' ':
        contEspaco +=1

#calculando o resto
contResto = len(frase) - (contVogais+contEspaco)

#resultado
print(f'Total de vogais na frase: {contVogais}')
print(f'Total de espaços na frase: {contEspaco}')
print(f'Resto: {contResto}')