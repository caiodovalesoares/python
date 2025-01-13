chessboard = []
for i in range(10):
    chessboard.append([])
    for j in range(10):
        chessboard[i].append(' ')

for i in range(1, 9):
    for j in range(1, 9):
        print(f'[{chessboard[i][j]:^1}]', end='')
    print()

queenLine = int(input('Digite em qual linha (de 1 a 8) você deseja posicionar sua rainha: '))
queenColumn = int(input('Digite em qual coluna (de 1 a 8) você deseja posicionar sua rainha: '))

if queenLine >= queenColumn:
    dif = queenLine - queenColumn
else:
    dif = queenColumn - queenLine

for i in range(10):
    for j in range(10):
        if i == 0 or i == 9 or j == 0 or j == 9: chessboard[i][j] = '+'

for i in range(1, 9):
    for j in range(1, 9):
        if i == queenLine or j == queenColumn or abs(i - queenLine) == abs(j - queenColumn):
            chessboard[i][j] = 'o'
        if i == queenLine and j == queenColumn:
            chessboard[i][j] = 'Q'
        print(f'[{chessboard[i][j]:^1}]', end='')
    print()

option = 1
while option != 2:
    print('=-' * 30)
    option = int(input('(1) para mover a rainha\n(2) para encerrar o programa\nEscolha uma opção: '))
    if option == 1:
        queenLine = int(input('Digite em qual linha (que contenha "o") você deseja posicionar sua rainha: '))
        queenColumn = int(input('Digite em qual coluna (que contenha "o") você deseja posicionar sua rainha: '))

        if chessboard[queenLine][queenColumn] != 'o':
            print('Posição inválida!')
            continue
        else:
            for i in range(1, 9):
                for j in range(1, 9):
                    chessboard[i][j] = ' '

        if queenLine >= queenColumn:
            dif = queenLine - queenColumn
        else:
            dif = queenColumn - queenLine

        for i in range(10):
            for j in range(10):
                if i == 0 or i == 9 or j == 0 or j == 9: chessboard[i][j] = '+'

        for i in range(1, 9):
            for j in range(1, 9):
                if i == queenLine or j == queenColumn or abs(i - queenLine) == abs(j - queenColumn):
                    chessboard[i][j] = 'o'
                if i == queenLine and j == queenColumn:
                    chessboard[i][j] = 'Q'
                print(f'[{chessboard[i][j]:^1}]', end='')
            print()
    if option == 2:
        print('Fim do programa!')
    if option != 1 and option != 2:
        print('Opção inválida!')