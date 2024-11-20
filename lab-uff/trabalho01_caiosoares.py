# Nome: Caio do Vale Soares
# Data: 18/11/2024
# Programa que calcula o IMC (Índice de Massa Corporal) de uma pessoa baseado na sua altura e no seu peso

idade = int(input('Digite a sua idade: '))

#adultos com 20 anos ou mais
if idade >= 20:
    peso = float(input('Digite seu peso: '))
    altura = float(input('Digite sua altura: '))
    #calculando o imc
    imc = peso / (altura**2)

    #classificando os adultos de acordo com o imc
    if imc <= 18.5:
        print('Seu imc é ', imc, ' e você está abaixo do peso ideal')
    if imc > 18.5 and imc <= 25:
        print('Seu imc é ', imc, ' e você está com o peso adequado')
    if imc > 25 and imc <= 30:
        print('Seu imc é ', imc, ' e você está com uma pré-obesidade')
    if imc > 30 and imc <= 35:
        print('Seu imc é ', imc, ' e você está com obesidade grau 1')
    if imc > 35 and imc <= 40:
        print('Seu imc é ', imc, ' e você está com obesidade grau 2')
    if imc > 40:
        print('Seu imc é ', imc, ' e você está com obesidade grau 3')

#adolescentes com menos de 20 anos
if idade < 20:
    sexo = str(input('Digite o seu sexo ((M)asculino ou (F)eminino): '))
    peso = float(input('Digite seu peso: '))
    altura = float(input('Digite sua altura: '))
    #calculando o imc
    imc = peso / (altura**2)

    #adolescentes do sexo masculino
    if sexo == 'M' or sexo == 'm':
        #separando por idade
        if idade == 10:
            #classificando de acordo com o imc
            if imc <= 14.42:
                print('Seu imc é ', imc, ' e você está com baixo peso')
            if imc > 14.42 and imc < 19.60:
                print('Seu imc é ', imc, ' e você está com um peso adequado')
            if imc >= 19.60:
                print('Seu imc é ', imc, ' e você está com sobrepeso')
        if idade == 11:
            if imc <= 14.83:
                print('Seu imc é ', imc, ' e você está com baixo peso')
            if imc > 14.83 and imc < 20.35:
                print('Seu imc é ', imc, ' e você está com um peso adequado')
            if imc >= 20.35:
                print('Seu imc é ', imc, ' e você está com sobrepeso')
        if idade == 12:
            if imc <= 15.24:
                print('Seu imc é ', imc, ' e você está com baixo peso')
            if imc > 15.24 and imc < 21.12:
                print('Seu imc é ', imc, ' e você está com um peso adequado')
            if imc >= 21.12:
                print('Seu imc é ', imc, ' e você está com sobrepeso')
        if idade == 13:
            if imc <= 15.73:
                print('Seu imc é ', imc, ' e você está com baixo peso')
            if imc > 15.73 and imc < 21.93:
                print('Seu imc é ', imc, ' e você está com um peso adequado')
            if imc >= 21.93:
                print('Seu imc é ', imc, ' e você está com sobrepeso')
        if idade == 14:
            if imc <= 16.18:
                print('Seu imc é ', imc, ' e você está com baixo peso')
            if imc > 16.18 and imc < 22.77:
                print('Seu imc é ', imc, ' e você está com um peso adequado')
            if imc >= 22.77:
                print('Seu imc é ', imc, ' e você está com sobrepeso')
        if idade == 15:
            if imc <= 16.59:
                print('Seu imc é ', imc, ' e você está com baixo peso')
            if imc > 16.59 and imc < 23.63:
                print('Seu imc é ', imc, ' e você está com um peso adequado')
            if imc >= 23.63:
                print('Seu imc é ', imc, ' e você está com sobrepeso')
        if idade == 16:
            if imc <= 17.01:
                print('Seu imc é ', imc, ' e você está com baixo peso')
            if imc > 17.01 and imc < 24.45:
                print('Seu imc é ', imc, ' e você está com um peso adequado')
            if imc >= 24.45:
                print('Seu imc é ', imc, ' e você está com sobrepeso')
        if idade == 17:
            if imc <= 17.31:
                print('Seu imc é ', imc, ' e você está com baixo peso')
            if imc > 17.31 and imc < 25.28:
                print('Seu imc é ', imc, ' e você está com um peso adequado')
            if imc >= 25.28:
                print('Seu imc é ', imc, ' e você está com sobrepeso')
        if idade == 18:
            if imc <= 17.54:
                print('Seu imc é ', imc, ' e você está com baixo peso')
            if imc > 17.54 and imc < 25.95:
                print('Seu imc é ', imc, ' e você está com um peso adequado')
            if imc >= 25.95:
                print('Seu imc é ', imc, ' e você está com sobrepeso')
        if idade == 19:
            if imc <= 17.80:
                print('Seu imc é ', imc, ' e você está com baixo peso')
            if imc > 17.80 and imc < 26.36:
                print('Seu imc é ', imc, ' e você está com um peso adequado')
            if imc >= 26.36:
                print('Seu imc é ', imc, ' e você está com sobrepeso')

    #adolescentes do sexo feminino
    if sexo == 'F' or sexo == 'f':
        #separando por idade
        if idade == 10:
            #classificando de acordo com o imc
            if imc <= 14.23:
                print('Seu imc é ', imc, ' e você está com baixo peso')
            if imc > 14.23 and imc < 20.19:
                print('Seu imc é ', imc, ' e você está com um peso adequado')
            if imc >= 20.19:
                print('Seu imc é ', imc, ' e você está com sobrepeso')
        if idade == 11:
            if imc <= 14.60:
                print('Seu imc é ', imc, ' e você está com baixo peso')
            if imc > 14.60 and imc < 21.18:
                print('Seu imc é ', imc, ' e você está com um peso adequado')
            if imc >= 21.18:
                print('Seu imc é ', imc, ' e você está com sobrepeso')
        if idade == 12:
            if imc <= 14.98:
                print('Seu imc é ', imc, ' e você está com baixo peso')
            if imc > 14.98 and imc < 22.17:
                print('Seu imc é ', imc, ' e você está com um peso adequado')
            if imc >= 22.17:
                print('Seu imc é ', imc, ' e você está com sobrepeso')
        if idade == 13:
            if imc <= 15.36:
                print('Seu imc é ', imc, ' e você está com baixo peso')
            if imc > 15.36 and imc < 23.08:
                print('Seu imc é ', imc, ' e você está com um peso adequado')
            if imc >= 23.08:
                print('Seu imc é ', imc, ' e você está com sobrepeso')
        if idade == 14:
            if imc <= 15.67:
                print('Seu imc é ', imc, ' e você está com baixo peso')
            if imc > 15.67 and imc < 23.88:
                print('Seu imc é ', imc, ' e você está com um peso adequado')
            if imc >= 23.88:
                print('Seu imc é ', imc, ' e você está com sobrepeso')
        if idade == 15:
            if imc <= 16.01:
                print('Seu imc é ', imc, ' e você está com baixo peso')
            if imc > 16.01 and imc < 24.29:
                print('Seu imc é ', imc, ' e você está com um peso adequado')
            if imc >= 24.29:
                print('Seu imc é ', imc, ' e você está com sobrepeso')
        if idade == 16:
            if imc <= 16.37:
                print('Seu imc é ', imc, ' e você está com baixo peso')
            if imc > 16.37 and imc < 24.74:
                print('Seu imc é ', imc, ' e você está com um peso adequado')
            if imc >= 24.74:
                print('Seu imc é ', imc, ' e você está com sobrepeso')
        if idade == 17:
            if imc <= 16.59:
                print('Seu imc é ', imc, ' e você está com baixo peso')
            if imc > 16.59 and imc < 25.23:
                print('Seu imc é ', imc, ' e você está com um peso adequado')
            if imc >= 25.23:
                print('Seu imc é ', imc, ' e você está com sobrepeso')
        if idade == 18:
            if imc <= 16.71:
                print('Seu imc é ', imc, ' e você está com baixo peso')
            if imc > 16.71 and imc < 25.56:
                print('Seu imc é ', imc, ' e você está com um peso adequado')
            if imc >= 25.56:
                print('Seu imc é ', imc, ' e você está com sobrepeso')
        if idade == 19:
            if imc <= 16.87:
                print('Seu imc é ', imc, ' e você está com baixo peso')
            if imc > 16.87 and imc < 25.85:
                print('Seu imc é ', imc, ' e você está com um peso adequado')
            if imc >= 25.85:
                print('Seu imc é ', imc, ' e você está com sobrepeso')