with open('c:/Users/caiod/OneDrive/Documentos/estudos/python/prog1-uff/lista04/conta.txt', 'r') as archive:
    calculator = archive.readlines()

calculator = [line.strip() for line in calculator if line.strip()]

for i in range(0, len(calculator), 2):
    calculator[i] = float(calculator[i])

total = calculator[0]
for i in range(1, len(calculator), 2):
    if calculator[i] == '+':
        total += calculator[i+1]
    elif calculator[i] == '-':
        total -= calculator[i+1]
    elif calculator[i] == '*':
        total *= calculator[i+1]
    elif calculator[i] == '/':
        total /= calculator[i+1]

print(f'Resultado: {total:.2f}')