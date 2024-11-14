# Nome: Caio do Vale Soares
# Data: 13/11/2024
# Programa que imprime os primeiros N números que são primos e estão na sequência de fibonacci

#variáveis
num = 1
fib = 1
contFib = 0

n = int(input('Digite quantos números você deseja: '))
while contFib < n:
    
    #sequência de fibonacci
    for i in range(1,n+1):
        contDiv = 0
        fib += num

        #verificando se o número é primo
        for j in range(2, fib):
            if fib % j == 0:
                contDiv += 1
        if contDiv == 0:
            contFib +=1
            print(fib)
        num = fib - num
    