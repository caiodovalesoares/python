with open('python/prog1-uff/lista04/respostas.txt', 'r') as archive:
    answers = archive.readlines()

smoker = 0
nonSmoker = 0
under40NonSmoker = 0
over40Smoker = 0
menTotal = 0
womenTotal = 0
for i in range(len(answers)):
    if 'S' in answers[i]:
        smoker += 1
        if int(answers[i][2:4]) > 40 and 'F' in answers[i]:
            over40Smoker += 1
    if 'N' in answers[i]:
        nonSmoker += 1
        if int(answers[i][2:4]) < 40 and 'M' in answers[i]:
            under40NonSmoker += 1
    if 'M' in answers[i]:
        menTotal += 1
    if 'F' in answers[i]:
        womenTotal += 1

smokersPercentual = smoker / len(answers)
under40NonSmokerPercentual = under40NonSmoker / menTotal
over40SmokerPercentual = over40Smoker / womenTotal

print(f'Percentual de fumantes: {smokersPercentual:.2%}')
print(f'Percentual de homens não fumantes abaixo de 40 anos: {under40NonSmokerPercentual:.2%}')
print(f'Percentual de mulheres fumantes acima de 40 anos: {over40SmokerPercentual:.2%}')