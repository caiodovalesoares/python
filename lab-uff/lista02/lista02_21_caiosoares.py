# Nome: Caio do Vale Soares
# Data: 11/12/24
# Programa que inverte as letras minúsculas de um arquivo .txt por maiúsculas e vice-versa

import unicodedata

with open('entrada.txt', 'w', encoding = 'utf-8') as arq:
  arq.write('Sou Tricolor de coração Sou do clube tantas vezes campeão Fascina pela sua disciplina, o Fluminense me domina Eu tenho amor ao Tricolor Salve o querido pavilhão Das três cores que traduzem tradição A paz, a esperança e o vigor, unido e forte pelo esporte Eu sou é Tricolor')

with open('entrada.txt', 'r') as entrada:
  conteudo = entrada.read()

#removendo acentuação
conteudo = unicodedata.normalize('NFKD', conteudo).encode('ASCII', 'ignore').decode('ASCII')
saida = conteudo.swapcase()

with open('saida.txt', 'w') as arquivo_saida:
  arquivo_saida.write(saida)

#resultado
print(saida)