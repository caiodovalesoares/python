# Nome: Caio do Vale Soares
# Data: 02/11/2024
# Programa que calcula a área de um triângulo qualquer, usando apenas as medidas dos lados

#variável para controlar loop
valido = False

#comprimentos dos lados do triângulo
while not valido:
    a = float(input("Digite o comprimento do lado A: "))
    b = float(input("Digite o comprimento do lado B: "))
    c = float(input("Digite o comprimento do lado C: "))

    if a > 0 and b > 0 and c > 0:
        valido = True
    else:
        print("Medidas inválidas! Os lados devem ser maiores que 0.")

#verificando se é um triângulo válido
if a + b > c and a + c > b and b + c > a:
    #semi-perímetro
    s = (a + b + c) / 2
    
    #calculando a área usando fórmula de Heron
    area = (s * (s - a) * (s - b) * (s - c)) ** 0.5
    
    #resultado
    print("A área do triângulo é:", area)
else:
    print("Medidas inválidas! Não forma um triângulo.")