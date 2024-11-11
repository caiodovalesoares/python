# Nome: Caio do Vale Soares
# Data: 02/11/2024
# Programa que lê a resposta de consumidores e depois apresenta as porcentagens 

#variáveis
sim = 0
nao = 0
finalizado = False

#respostas
while not finalizado:
    resposta = input("Digite sua resposta (S/N) ou F para finalizar: ")

    if resposta == 'F' or resposta == 'f':
        finalizado = True
    elif resposta == 'S' or resposta == 's':
        sim += 1
    elif resposta == 'N' or resposta == 'n':
        nao += 1
    else:
        print("Resposta inválida. Por favor, digite S, N ou F.")

total_respostas = sim + nao

#calculando as porcentagens
if total_respostas > 0:
    porcentagem_sim = (sim / total_respostas) * 100
    porcentagem_nao = (nao / total_respostas) * 100

#resultado final
    print("Porcentagem de satisfação: %.2f%%" % porcentagem_sim)
    print("Porcentagem de insatisfação: %.2f%%" % porcentagem_nao)
else:
    print("Nenhuma resposta registrada.")
