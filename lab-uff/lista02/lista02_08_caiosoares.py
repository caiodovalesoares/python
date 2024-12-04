# Nome: Caio do Vale Soares
# Data: 02/12/24
# Programa que recebe uma matriz e a transforma em uma matriz transposta

#função matriz transposta
def mat_transposta(matriz):
    return [[linha[i] for linha in matriz] for i in range(len(matriz[0]))]

#lendo o número de linhas e colunas
def main():
    linhas = int(input("Digite o número de linhas: "))
    colunas = int(input("Digite o número de colunas: "))

    matriz = []

    #lendos os elementos da matriz
    for i in range(linhas):
        linha = []
        for j in range(colunas):
            linha.append(int(input(f'Digite o elemento [{i+1}][{j+1}]: ')))
        matriz.append(linha)
    
    #printando a matriz original
    print("\nMatriz original:")
    for linha in matriz:
        print(linha)

    transposta = mat_transposta(matriz)

    #printando matriz transposta
    print("\nMatriz transposta:")
    for linha in transposta:
        print(linha)

if __name__ == "__main__":
    main()