# Nome: Caio do Vale Soares
# Data: 13/11/2024
# Programa que calcula um financiamento

#dados do financiamento
pmt = float(input('Digite o valor das parcelas: '))
juros = float(input('Digite o juros em porcentagem: '))
porcentagem = juros / 100
n = int(input('Digite a quantidade de parcelas: '))
soma = 0

#somatória
for i in range(1,n+1):
    soma += pmt / (1+porcentagem)**i

#resultado
print('Valor final: ', soma)