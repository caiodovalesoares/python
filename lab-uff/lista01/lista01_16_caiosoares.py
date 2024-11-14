# Nome: Caio do Vale Soares
# Data: 13/11/2024
#Programa que lê o sexo e a resposta de funcionários de uma empresa e depois retorna a quantidade de pessoas que responderam sim, que responderam não e a porcentagem de homens que responderam não

#variáveis
contHomens = 0
contSim = 0
contNao = 0

#dados dos funcionários
for i in range(1,21):
    sexo = str(input('Digite o sexo (M ou F) do funcionário: '))
    resp = str(input('Digite a resposta (sim ou nao) do funcionário: '))

    #homens que responderam não
    if (sexo == 'm' or sexo == 'M') and (resp == 'nao' or resp == 'NAO'):
        contHomens += 1

    #pessoas que responderam sim ou não
    if resp == 'SIM' or resp == 'sim':
        contSim += 1
    if resp == 'NAO' or resp == 'nao':
        contNao += 1

#cálculo da porcentagem
homemNao = (contHomens/20) * 100

#resultado
print('Pessoas que responderam sim: ', contSim)
print('Pessoas que responderam nao: ', contNao)
print('Porcentagem de homens que responderam não: ', homemNao, '%')