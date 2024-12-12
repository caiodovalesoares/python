# Nome: Caio do Vale Soares
# Data: 11/12/24
# Programa que conta quantas vezes cada letra aparece num arquivo .txt

import unicodedata

#criando arquivo
with open('entrada.txt', 'w', encoding='utf-8') as entrada1:
    entrada1.write('Sou Tricolor de coração Sou do clube tantas vezes campeão')

with open('entrada.txt', 'r', encoding='utf-8') as entrada1:
    entrada = entrada1.read()

#preparando texto
entrada = entrada.upper()
entrada = unicodedata.normalize('NFKD', entrada).encode('ASCII', 'ignore').decode('ASCII')
entrada = entrada.replace(' ', '')

#contando letras
letras_contadas = {}
for letra in entrada:
    if letra in letras_contadas:
        letras_contadas[letra] += 1
    else:
        letras_contadas[letra] = 1

#gravando resultado
with open('saida.txt', 'w', encoding='utf-8') as saida1:
    for letra, contador in letras_contadas.items():
        saida1.write(f'{letra} {contador}\n')

#lendo resultado
with open('saida.txt', 'r', encoding='utf-8') as saida1:
    saida = saida1.read()

print(saida)