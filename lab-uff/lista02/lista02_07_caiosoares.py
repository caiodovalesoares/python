# Nome: Caio do Vale Soares
# Data: 02/12/24
# Programa que cria uma função que diz se as duas frases digitadas são anagramas

import unicodedata

frase1 = str(input('Digite a primeira frase: '))
frase2 = str(input('Digite a segunda frase: '))

#tirando acentuação e passando as frases para letras minúsculas
frase1 = frase1.lower()
frase1 = unicodedata.normalize('NFKD', frase1).encode('ASCII', 'ignore').decode('ASCII')

frase2 = frase2.lower()
frase2 = unicodedata.normalize('NFKD', frase2).encode('ASCII', 'ignore').decode('ASCII')

#função anagrama
def anagrama(frase1, frase2):
    if len(frase1) != len(frase2):
        return False
    else:
        for i in range(0, len(frase1)):
            if frase1[i] in frase2:
                return True
            else:
                return False

#resultado
print('As palavras são anagramas?'); print(anagrama(frase1, frase2))