# Nome: Caio do Vale Soares
# Data: 11/12/24
# Programa que calcula a área de um polígono convexo

#função que calcula a área do triângulo
def area_triangulo(mat):
 x1, y1 = mat[0]
 x2, y2 = mat[1]
 x3, y3 = mat[2]
 a = ((x2-x1)**2 + (y2-y1)**2)**0.5
 b = ((x3-x2)**2 + (y3-y2)**2)**0.5
 c = ((x1-x3)**2 + (y1-y3)**2)**0.5
 s = (a + b + c) / 2
 return (s * (s-a) * (s-b) * (s-c)) ** 0.5

#função que calcula a área do polígono
def area_poligono(matriz):
 if len(matriz) < 3:
    #mensagem de erro
    raise ValueError("Polígono deve ter pelo menos 3 vértices")
 
 area_total = 0
 primeiro_vertice = matriz[0]
 
 for i in range(1, len(matriz) - 1):
    triangulo = [primeiro_vertice, matriz[i], matriz[i+1]]
    area_total += area_triangulo(triangulo)
 
 return area_total

def main():
 print("Calculadora de Área de Polígono")
 
 num_vertices = int(input("Informe o número de vértices: "))
 
 vertices = []
 #vertices
 for i in range(num_vertices):
    x = float(input(f"Informe o x do vértice {i+1}: "))
    y = float(input(f"Informe o y do vértice {i+1}: "))
    vertices.append([x, y])
 #resultado
 area = area_poligono(vertices)
 print(f"Área do polígono: {area:.2f}")

if __name__ == "__main__":
   main()
