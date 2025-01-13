import csv

# Lendo o arquivo inteiro
with open('exemplo.txt', 'r') as arquivo:
    conteudo = arquivo.read()
    print(conteudo)

# Lendo linha por linha
with open('exemplo.txt', 'r') as arquivo:
    for linha in arquivo:
        print(linha.strip())

# Lendo todas as linhas em uma lista
with open('exemplo.txt', 'r') as arquivo:
    linhas = arquivo.readlines()
    for linha in linhas:
        print(linha.strip())

# Lendo linha por linha usando readline()
with open('exemplo.txt', 'r') as arquivo:
    print('Lendo linha por linha (usando readline()):')
    while True:
        linha = arquivo.readline()
        if not linha:
            break
        print(linha.strip())

# Escrevendo em um arquivo (sobrescreve o arquivo se ele já existir)
with open('exemplo.txt', 'w') as arquivo:
    arquivo.write('Olá, mundo!\n')

# Anexando ao final de um arquivo
with open('exemplo.txt', 'a') as arquivo:
    arquivo.write('Adicionando uma nova linha.\n')

    # Escrevendo em um arquivo CSV
    with open('exemplo.csv', 'w', newline='') as csvfile:
        escritor = csv.writer(csvfile)
        escritor.writerow(['Nome', 'Idade', 'Cidade'])
        escritor.writerow(['Alice', 30, 'São Paulo'])
        escritor.writerow(['Bob', 25, 'Rio de Janeiro'])
        escritor.writerow(['Charlie', 35, 'Belo Horizonte'])

    # Lendo um arquivo CSV
    with open('exemplo.csv', 'r') as csvfile:
        leitor = csv.reader(csvfile)
        for linha in leitor:
            print(', '.join(linha))

    # Escrevendo em um arquivo CSV usando DictWriter
    with open('exemplo_dict.csv', 'w', newline='') as csvfile:
        campos = ['Nome', 'Idade', 'Cidade']
        escritor = csv.DictWriter(csvfile, fieldnames=campos)
        escritor.writeheader()
        escritor.writerow({'Nome': 'Alice', 'Idade': 30, 'Cidade': 'São Paulo'})
        escritor.writerow({'Nome': 'Bob', 'Idade': 25, 'Cidade': 'Rio de Janeiro'})
        escritor.writerow({'Nome': 'Charlie', 'Idade': 35, 'Cidade': 'Belo Horizonte'})

    # Lendo um arquivo CSV usando DictReader
    with open('exemplo_dict.csv', 'r') as csvfile:
        leitor = csv.DictReader(csvfile)
        for linha in leitor:
            print(f"Nome: {linha['Nome']}, Idade: {linha['Idade']}, Cidade: {linha['Cidade']}")