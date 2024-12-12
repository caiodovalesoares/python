# Nome: Caio do Vale Soares
# Data: 11/12/24
# Programa que converte números romanos menores que 4000 para arábicos

while True:
    print("1. Converter número romano")
    print("2. Sair")
    escolha = input("Escolha uma opção: ")

    if escolha == "1":
        romano = input("Informe um número romano (menor que 4000): ")
    if escolha == "2":
            break
    if romano.isalpha() and len(romano) > 0:
        romano = romano.upper()
    valores = {
    'M': 1000,
    'CM': 900,
    'D': 500,
    'CD': 400,
    'C': 100,
    'XC': 90,
    'L': 50,
    'XL': 40,
    'X': 10,
    'IX': 9,
    'V': 5,
    'IV': 4,
    'I': 1
    }

    resultado = 0
    i = 0
    while i < len(romano):
        if i + 1 < len(romano) and romano[i:i+2] in valores:
            resultado += valores[romano[i:i+2]]
            i += 2
        elif romano[i] in valores:
            resultado += valores[romano[i]]
            i += 1
        else:
            print("Algarismo romano inválido")
            break
    
        if resultado < 4000:
            print(resultado)
    
    else:
        print("Número romano deve ser menor que 4000")

    