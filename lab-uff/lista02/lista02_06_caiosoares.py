# Nome: Caio do Vale Soares
# Data: 27/11/24
# Programa que cria uma função que retorna True se uma string for um palíndromo e False se não for

#biblioteca math para arredondar o índice
import math as m

palavra = str(input('Digite: '))

#função palíndromo
def palindromo(palavra):
    i = len(palavra) / 2
    i = m.ceil(i)
    #comparando a primeira e a segunda metade da string
    if palavra[i-2::-1] in palavra[i:i*2]:
        return True
    else:
        return False

#resultado
print('A string é um palíndromo?'); print(palindromo(palavra))