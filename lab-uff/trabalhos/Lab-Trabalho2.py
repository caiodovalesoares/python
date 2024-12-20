# Nome: Caio do Vale Soares
# Turma: TCC00355 - LABORATÓRIO DE RESOLUÇÃO DE PROBLEMAS - EA
# Data de criação: 15/12/24 - 20/12/24
# Programa que lê uma relação de nomes de alunos e suas respectivas notas. A relação acaba quando o usuário apresenta uma nota negativa (que não deve ser considerada).

#biblioteca math para calcular o desvio padrão e a mediana
import math as m
import sys

#variável e listas para inicialização do programa
nota = 0
alunos = ['caio', 'bia', 'theo', 'maria', 'leo']
notas = [7.2, 8.0, 7.2, 6.0, 5.4]

#ordem alfabética
ordem_alfabetica = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

#estrutura de repetição para identificar notas negativas
while nota >= 0:
    #opções para o usuário
    print('=-' * 30)
    print('1) Apresentar as estatísticas sobre as notas: máxima, mínima, média, desvio padrão, mediana e moda\n2) Apresentar uma relação de alunos (ordenada por nota) e respectivas notas que estejam dentro de uma faixa de valores (máximo e mínimo)\n3) Apresentar uma relação de alunos e respectivas notas (ordenada por nome), cujos nomes dos alunos contenham uma string informada pelo usuário\n4) Apresentar uma relação de notas e respectivas frequências (número de ocorrências), para uma faixa de valores (máximo e mínimo)\n5) Incluir um novo aluno/nota\n6) Terminar o programa')
    resp = int(input('Digite a opção desejada: '))
    if resp > 0 and resp < 7:
        match resp:
            case 1: 
                #variáveis para inicialização
                maior_nota = 0
                menor_nota = 99999
                soma_notas = 0
                moda = -1
                desvio = 0

                #ordenando a lista
                notas_reserva = notas.copy()
                notas_reserva.sort()

                moda_alunos = []
                qtd_moda = []
                for i in range(0, len(notas_reserva)):
                    #maior e menor nota
                    if notas_reserva[i] > maior_nota:
                        maior_nota = notas_reserva[i]
                    if notas_reserva[i] < menor_nota:
                        menor_nota = notas_reserva[i]

                    #soma das notas
                    soma_notas += notas_reserva[i]

                    #mediana
                    if len(notas_reserva) % 2 == 0:
                        num = m.ceil(len(notas_reserva) / 2)
                        mediana = (notas_reserva[num-1] + notas_reserva[num]) / 2
                    else:
                        num = m.floor(len(notas_reserva) / 2)
                        mediana = notas_reserva[num]

                #moda
                for i in range(len(notas_reserva)):
                    if notas_reserva.count(notas_reserva[i]) == moda and notas_reserva[i] not in moda_alunos:
                        moda_alunos.append(notas_reserva[i])
                        qtd_moda.append(notas_reserva.count(notas_reserva[i]))
                    if notas_reserva.count(notas_reserva[i]) > moda:
                        moda = notas_reserva.count(notas_reserva[i])
                        moda_alunos.clear()
                        moda_alunos.append(notas_reserva[i])
                        qtd_moda.clear()
                        qtd_moda.append(notas_reserva.count(notas_reserva[i]))
                
                #média das notas
                media = soma_notas / len(notas_reserva)

                #desvio padrão
                for i in range(len(notas_reserva)):
                    n = (notas_reserva[i]-media) ** 2
                    desvio += n
                    desvio = m.sqrt(desvio/len(notas_reserva))

                #estatísticas desejadas
                print('=-' * 30)
                print(f'Maior nota da turma: {maior_nota}')
                print(f'Menor nota da turma: {menor_nota}')
                print(f'Média da turma: {media:.2f}')
                print(f'Desvio padrão da turma: {desvio:.2f}')
                print(f'Mediana da turma: {mediana}')
                print(f'Moda da turma: {moda_alunos}, Frequência: {qtd_moda}')

            case 2:
                #valores mínimo e máximo
                minimo = int(input('Digite o valor mínimo: '))
                maximo = int(input('Digite o valor máximo: '))

                #ordenando a lista
                for i in range(len(notas)):
                    for j in range(len(notas)):
                        if notas[i] > notas[j]:
                            notas[i], notas[j] = notas[j], notas[i]
                            alunos[i], alunos[j] = alunos[j], alunos[i]
                
                #exibindo a lista
                print('=-' * 30)
                for i in range((len(notas) - 1), -1, -1):
                    if notas[i] >= minimo and notas[i] <= maximo:
                        print(f'{notas[i]}, Aluno: {alunos[i]}')

            case 3:
                #ordenando a lista em ordem alfabética
                for i in range(len(notas)):
                        for j in range((len(notas)) - 1):
                            alunos[j] = alunos[j].lower()
                            for k in range(len(alunos[j])):
                                l = 0
                                nome1 = alunos[j]
                                nome2 = alunos[j+1]
                                if ordem_alfabetica.index(nome1[l]) > ordem_alfabetica.index(nome2[l]):
                                    notas[j], notas[j+1] = notas[j+1], notas[j]
                                    alunos[j], alunos[j+1] = alunos[j+1], alunos[j]
                                    break
                                if ordem_alfabetica.index(nome1[l]) == ordem_alfabetica.index(nome2[l]):
                                    l += 1

                #lendo a string desejada
                string = str(input('Digite a string desejada: '))

                #exibindo a lista
                print('=-' * 30)
                contador_alunos = 0
                #checando se a string está vazia
                if string != None:
                    for i in range(len(alunos)):
                        if string in alunos[i]:
                            print(f'{alunos[i]}, Nota: {notas[i]}')
                            contador_alunos += 1
                    #checando se existem alunos com a string informada
                    if contador_alunos == 0:
                            print('Não há nenhum aluno com a string desejada.')
                else:
                    for i in range(len(alunos)):
                        print(f'{alunos[i]}, Nota: {notas[i]}')

            case 4:
                #ordenando a lista
                notas.sort()
                #valores mínimo e máximo
                minimo = int(input('Digite o valor mínimo: '))
                maximo = int(input('Digite o valor máximo: '))

                #exibindo a lista
                print('=-' * 30)
                for i in range(len(notas)):
                    if notas[i] >= minimo and notas[i] <= maximo and notas.count(notas[i]) > 1 and notas[i] != notas[i-1]:
                        print(f'Nota {notas[i]}, {notas.count(notas[i])} vezes')
                    if notas[i] >= minimo and notas[i] <= maximo and notas.count(notas[i]) == 1:
                        print(f'Nota {notas[i]}, 1 vez')

            #adicionando novo aluno e sua nota
            case 5:
                nota = (float(input('Digite a nota do aluno: ')))
                if nota >= 0:
                    notas.append(nota)
                    alunos.append(str(input('Digite o nome do aluno: ')))

            #encerrando o programa
            case 6:
                print('Fim do programa')
                break
    
    #mensagem de erro
    else:
        print("Opção inválida")

#encerrando o programa
else:
    print('Fim do programa')