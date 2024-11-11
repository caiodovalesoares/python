# Nome: Caio do Vale Soares
# Data: 02/11/2024
# Programa que faz a contagem de votos de uma eleição municipal

#fazendo contadores para cada candidato, votos brancos e nulos
votos_joao = 0
votos_jose = 0
votos_maria = 0
votos_pedro = 0
votos_brancos = 0
votos_nulos = 0

#total de eleitores
total_eleitores = 20000

#recebendo e contando votos
for i in range(total_eleitores):
    voto = int(input("Digite o voto (1-4 para candidatos, 0 para branco, outro valor para nulo): "))
    
    if voto == 1:
        votos_joao += 1
    elif voto == 2:
        votos_jose += 1
    elif voto == 3:
        votos_maria += 1
    elif voto == 4:
        votos_pedro += 1
    elif voto == 0:
        votos_brancos += 1
    else:
        votos_nulos += 1

#resultado da apuração
print("Resultado da Apuração:")
print("João da Silva (1):", votos_joao)
print("José Ramalho (2):", votos_jose)
print("Maria Mattos (3):", votos_maria)
print("Pedro Américo (4):", votos_pedro)
print("Votos em branco:", votos_brancos)
print("Votos nulos:", votos_nulos)