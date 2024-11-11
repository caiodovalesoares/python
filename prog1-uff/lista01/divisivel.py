num = int(input('Digite um número: '))
match num:
    case num if num%10 == 0:
        print(f'{num} / 10 = {num//10}')
        print(f'{num} / 5 = {num//5}')
        print(f'{num} / 2 = {num//2}')
    case num if num%5 == 0:
        print(f'{num} / 5 = {num//5}')
    case num if num%2 == 0:
        print(f'{num} / 2 = {num//2}')
    case _:
        print(f'O número {num} não é divisível por 2, por 5 e nem por 10')