# Nome: Caio do Vale Soares
# Data: 07/12/24
# Programa que calcula as raízes de um sistema de 3 equações e 3 incógnitas pela regra de Cramer

#função para calcular determinante
def det(matriz):
 a, b, c = matriz[0]
 d, e, f = matriz[1]
 g, h, i = matriz[2]
 return a*(e*i - f*h) - b*(d*i - f*g) + c*(d*h - e*g)

#função para calcular raízes pelo método de Cramer
def cramer(matriz, vetor):
 if len(matriz) != len(matriz[0]):
    print("Erro: Matriz não é quadrada.")
    return []
 
 #verificando se o sistema tem solução
 det_matriz = det(matriz)
 if det_matriz == 0:
    print("Erro: Sistema não tem solução única.")
    return []
 
 #cálculo das raízes
 mat_x = [
 [vetor[0], matriz[0][1], matriz[0][2]],
 [vetor[1], matriz[1][1], matriz[1][2]],
 [vetor[2], matriz[2][1], matriz[2][2]]
 ]
 
 mat_y = [
 [matriz[0][0], vetor[0], matriz[0][2]],
 [matriz[1][0], vetor[1], matriz[1][2]],
 [matriz[2][0], vetor[2], matriz[2][2]]
 ]
 
 mat_z = [
 [matriz[0][0], matriz[0][1], vetor[0]],
 [matriz[1][0], matriz[1][1], vetor[1]],
 [matriz[2][0], matriz[2][1], vetor[2]]
 ]
 
 x = det(mat_x) / det_matriz
 y = det(mat_y) / det_matriz
 z = det(mat_z) / det_matriz
 
 return [x, y, z]

def main():
 print("Resolução de Sistema Linear pelo Método de Cramer")
 
 #entrada de dados
 ordem = 3
 matriz = []
 for i in range(ordem):
    linha = input(f"Digite os {ordem} elementos da linha {i+1}, separados por espaços: ")
    matriz.append(list(map(float, linha.split())))
 
 vetor = input("Digite os elementos do vetor, separados por espaços: ")
 vetor = list(map(float, vetor.split()))
 
 #verificando se vetor tem tamanho correto
 if len(vetor) != ordem:
    print("Erro: Vetor com tamanho incorreto.")
    return
 
 solução = cramer(matriz, vetor)
 print("Solução:", solução)

if __name__ == "__main__":
    main()