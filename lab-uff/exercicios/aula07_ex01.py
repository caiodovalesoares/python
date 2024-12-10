import math as m

raio = float(input('Digite o raio do círculo: '))
areaCirculo = m.pi * (raio**2)
volumeEsfera = (4/3) * m.pi * (raio**3)
print(f'Área do círculo com raio {raio}: {areaCirculo:.2f}')
print(f'Volume da esfera com raio {raio}: {volumeEsfera:.2f}')