# Nome: Caio do Vale Soares
# Data: 11/12/24
# Programa que lê um arquivo.txt e conta quantas vezes cada palavra aparece

import re

with open('nome_arquivo.txt', 'w', encoding = 'utf-8') as arquivo:
  arquivo.write('Sou Tricolor de coração '
'Sou do clube tantas vezes campeão '
'Fascina pela sua disciplina, o Fluminense me domina '
'Eu tenho amor ao Tricolor '

'Salve o querido pavilhão '
'Das três cores que traduzem tradição '
'A paz, a esperança e o vigor, unido e forte pelo esporte '
'Eu sou é Tricolor '

'Vence, o Fluminense '
'Com o verde da esperança '
'Pois quem espera sempre alcança '
'Clube que orgulha o Brasil '
'Retumbante de glórias e vitórias mil '

'Sou Tricolor de coração '
'Sou do clube tantas vezes campeão '
'Fascina pela sua disciplina, o Fluminense me domina '
'Eu tenho amor ao Tricolor '

'Salve o querido pavilhão '
'Das três cores que traduzem tradição '
'A paz, a esperança e o vigor, unido e forte pelo esporte '
'Eu sou é Tricolor '

'Vence, o Fluminense '
'Com o sangue do encarnado '
'Com amor e com vigor '
'Faz a torcida querida vibrar com a emoção do tricampeão '

'Vence, o Fluminense '
'Usando a fidalguia '
'Branco é paz e harmonia, brilha com o Sol da manhã '
'Com a luz de um refletor '
'Salve o Tricolor')

#função para ler o arquivo e pré-processar o texto
def ler_arquivo(nome_arquivo):
 with open('nome_arquivo.txt', 'r', encoding='utf-8') as arquivo:
    texto = arquivo.read()
 
 #removendo a pontuação e os números
 texto = re.sub(r'[^\w\s]', '', texto)
 
 #convertendo todas as palavras para minúsculas
 texto = texto.lower()
 
 return texto

#função para contar as palavras
def contar_palavras(texto):
 palavras = texto.split()
 contagem = {}
 
 for palavra in palavras:
    if palavra not in contagem:
        contagem[palavra] = 1
    else:
        contagem[palavra] += 1
 
 return contagem

#nome do arquivo
nome_arquivo = 'texto.txt'

#lendo o arquivo e pré-processar o texto
texto = ler_arquivo(nome_arquivo)

#contando as palavras
contagem_palavras = contar_palavras(texto)

#resultado
for palavra, contagem in contagem_palavras.items():
 print(f'{palavra}: {contagem}')