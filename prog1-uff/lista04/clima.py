with open('python/prog1-uff/lista04/temperatura.txt', 'r') as archive:
    temperature = archive.readlines()

totalTemp = 0
for i in range(len(temperature)):
    temperature[i] = float(temperature[i])
    totalTemp += temperature[i]

averageTemp = totalTemp / len(temperature)
maxTemp = max(temperature)
minTemp = min(temperature)

overAverage = 0
underAverage = 0
for i in range(len(temperature)):
    if temperature[i] > averageTemp:
        overAverage += 1
    elif temperature[i] < averageTemp: 
        underAverage += 1

print(f'Menor temperatura: {minTemp}')
print(f'Maior temperatura: {maxTemp}')
print(f'Temperatura média: {averageTemp:.2f}')
print(f'Número de dias abaixo da média: {underAverage}')
print(f'Número de dias acima da média: {overAverage}')