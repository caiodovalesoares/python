massa = int(input('Digite a massa do material, em gramas: '))

massaFinal = massa
segs = 0
while massaFinal > 0.5:
    massaFinal = massaFinal/2
    segs += 50

horas = segs//3600
minutos = (segs%3600)//60
segundos = (segs%3600)%60

print(f'Massa inicial: {massa}')
print(f'Massa final: {massaFinal}')
print(f'Tempo necessário para a massa ficar menor que 0.5 grama: {horas} horas, {minutos} minutos e {segundos} segundos')