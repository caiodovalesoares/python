# Nome: Caio do Vale Soares
# Data: 07/12/24
# Programa que calcula o valor de pi pela soma dos n primeiros termos da série estabelecida

import math

#função que calcula o valor de pi
def calcula_pi(n):
    soma = 0
    for i in range(1, n+1):
        termo = ((-1)**(i+1)) / (i**2)
        soma += termo
    return math.sqrt(12 * soma)

#lendo o número de termos
n = int(input("Digite o número de termos: "))
pi_calculado = calcula_pi(n)
pi_real = math.pi

#resultado
print(f"π calculado: {pi_calculado}")
print(f"π real: {pi_real}")
print(f"Erro: {abs(pi_real - pi_calculado)}")
