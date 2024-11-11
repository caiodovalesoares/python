# Nome: Caio do Vale Soares
# Data: 31/10/2024
# Programa que analisa os dados de funcionários de uma empresa

salarioMulher = 0
salarioHomem = 0
contMulher = 0
contHomem = 0
maior30 = 0

idade = int(input('Digite a idade do funcionário: '))
while idade > 0: #uma idade negativa encerra o programa
    sexo = str(input('Qual o sexo do funcionário? (m / f) '))
    salario = int(input('Digite o salário do funcionário: '))
    if sexo == "m":
        salarioHomem += salario
        contHomem += 1
    elif sexo == "f":
        salarioMulher += salario
        contMulher += 1
    if idade < 30 and salario > maior30:
        maior30 = salario
    idade = int(input('Digite a idade do funcionário: '))

#aqui eu calculei as médias salariais pedidas no problema
mediaHomem = salarioHomem / contHomem
mediaMulher = salarioMulher / contMulher

print('A média salarial dos homens dessa empresa é', mediaHomem)
print('A média salarial das mulheres dessa empresa é', mediaMulher)
print('O maior salário de um funcionário com menos de 30 anos é', maior30)