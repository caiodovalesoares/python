# Nome: Caio do Vale Soares
# Data: 24/10/2024
# Programa que faz a média do aluno após duas provas e diz se ele está aprovado

nota1 = float(input('Entre com a nota da P1:'))
nota2 = float(input('Entre com a nota da P2:')) # Aqui foi feita a leitura das notas do aluno
mediaDoAluno = (nota1+nota2)/2 # Para calcular a média, basta somar as duas notas e dividir por 2
if (mediaDoAluno >=7): # Se a média for maior ou igual a 7, o aluno está aprovado
    print('Aprovado com média:', mediaDoAluno)
print('Fim do programa!')