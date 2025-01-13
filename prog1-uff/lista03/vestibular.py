import random
import sys

answerKey = []
languages = []
math = []
natureSciences = []
socialSciences = []

answerKey.append(languages)
answerKey.append(math)
answerKey.append(natureSciences)
answerKey.append(socialSciences)

for _ in range(25):
    languages.append(random.choice('ab'))

for _ in range(25):
    math.append(random.choice('ab'))

for _ in range(25):
    natureSciences.append(random.choice('ab'))

for _ in range(25):
    socialSciences.append(random.choice('ab'))

studentAnswers = []
languages = []
math = []
natureSciences = []
socialSciences = []

studentAnswers.append(languages)
studentAnswers.append(math)
studentAnswers.append(natureSciences)
studentAnswers.append(socialSciences)

for _ in range(25):
    languages.append(random.choice('ab'))

for _ in range(25):
    math.append(random.choice('ab'))

for _ in range(25):
    natureSciences.append(random.choice('ab'))

for _ in range(25):
    socialSciences.append(random.choice('ab'))

totalRightAnswers = 0
for i in range(len(answerKey)):
    rightAnswers = 0
    for j in range(25):
        if answerKey[i][j] == studentAnswers[i][j]:
            rightAnswers += 1
    print(f'{rightAnswers} acertos na disciplina {i+1}')
    totalRightAnswers += rightAnswers
    if rightAnswers < 5:
        print(f'Reprovado! {rightAnswers} acertos na disciplina {i+1}!')
        exit()

if totalRightAnswers < 50:
    print(f'Reprovado! {totalRightAnswers} acertos totais!')
else:
    print(f'Parabéns, você foi aprovado com {totalRightAnswers} acertos')