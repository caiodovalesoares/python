with open('python/prog1-uff/lista04/respostas.txt', 'r') as archive:
    answers = archive.readlines()

people = []
for i in range(len(answers)):
    if 'M' in answers[i]:
        gender = 'Masculino'
    else:
        gender = 'Feminino'
    if 'S' in answers[i]:
        smoking = True
    else:
        smoking = False
    data = {
        'sexo': gender,
        'idade': int(answers[i][2:4]),
        'fumante': smoking
    }
    people.append(data)

smoker = 0
nonSmoker = 0
under40NonSmoker = 0
over40Smoker = 0
menTotal = 0
womenTotal = 0
for person in people:
    if person['fumante'] == True: 
        smoker += 1
    if person['sexo'] == 'Masculino':
        menTotal += 1
        if person['fumante'] == False and person['idade'] < 40:
            under40NonSmoker += 1
    elif person['sexo'] == 'Feminino':
        womenTotal += 1
        if person['idade'] > 40 and person['fumante'] == True:
            over40Smoker += 1


smokersPercentual = smoker / len(people)
under40NonSmokerPercentual = under40NonSmoker / menTotal
over40SmokerPercentual = over40Smoker / womenTotal

print(f'Percentual de fumantes: {smokersPercentual:.2%}')
print(f'Percentual de homens não fumantes abaixo de 40 anos: {under40NonSmokerPercentual:.2%}')
print(f'Percentual de mulheres fumantes acima de 40 anos: {over40SmokerPercentual:.2%}')