# Nome: Caio do Vale Soares
# Data: 11/12/24
# Programa que calcula a área de um triângulo utilizando a Fórmula de Heron

def area_triangulo(matriz):
    #verificando matriz válida
    if len(matriz) != 3 or any(len(ponto) != 2 for ponto in matriz):
        raise ValueError("Matriz inválida")

    x1, y1 = matriz[0]
    x2, y2 = matriz[1]
    x3, y3 = matriz[2]

    #comprimentos dos lados
    a = ((x2-x1)**2 + (y2-y1)**2)**0.5
    b = ((x3-x2)**2 + (y3-y2)**2)**0.5
    c = ((x1-x3)**2 + (y1-y3)**2)**0.5

    #semiperímetro
    s = (a + b + c) / 2

    #Fórmula de Heron
    area = (s * (s-a) * (s-b) * (s-c)) ** 0.5
    return area

matriz = [[0, 0], [3, 0], [1.5, 2.5]]
area = area_triangulo(matriz)

#resultado
print(f"Área do triângulo: {area:.2f}")
