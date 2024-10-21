number = int(input('Digite um número com 5 algarismos: '))

if (number%10) == (number//10000) and ((number%100) // 10) == ((number%10000) // 1000):
    print(f'O número {number} é um palíndromo!')
else:
    print(f'O número {number} não é um palíndromo!')