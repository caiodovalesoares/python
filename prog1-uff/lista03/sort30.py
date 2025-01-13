import random

numbers = []
for i in range(30):
    numbers.append(random.randint(1,50))

print(numbers)

# for i in range(len(numbers)):
#     for j in range(len(numbers)):
#         if i == j:
#             continue
#         if numbers[i] < numbers[j]:
#             numbers[i], numbers[j] = numbers[j], numbers[i]

auxNumbers = []
for i in range(len(numbers)):
    auxNumbers.append(min(numbers))
    numbers.remove(min(numbers))

numbers = auxNumbers.copy()

print(f'Lista ordenada: {numbers}')