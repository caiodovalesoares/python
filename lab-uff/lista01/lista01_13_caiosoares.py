# Nome: Caio do Vale Soares
# Data: 02/11/2024
# Programa que lê a idade de um grupo de pessoas e depois mostra a média e a porcentagem de pessoas entre 21 e 65 anos

#variáveis
soma_idades = 0
cont_pessoas = 0
cont_idade_valida = 0
fim = False

#lendo idades
while not fim:
    idade = int(input("Digite a idade (-1 para finalizar): "))

    if idade == -1:
        fim = True
    else:
        soma_idades += idade
        cont_pessoas += 1

        if 21 <= idade <= 65:
            cont_idade_valida += 1

#calculando média
if cont_pessoas > 0:
    media_idade = soma_idades / cont_pessoas
    porcentagem_idade_valida = (cont_idade_valida / cont_pessoas) * 100

    #resultado
    print("Idade média:", media_idade)
    print("Porcentagem de pessoas entre 21 e 65 anos:", porcentagem_idade_valida, "%")
else:
    print("Nenhuma idade registrada.")
