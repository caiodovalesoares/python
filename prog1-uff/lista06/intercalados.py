def intercalated(list1, list2):
    list3 = []
    for i in range(10):
        list3.append(list1[i])
        list3.append(list2[i])
    return list3

list1 = []
list2 = []
for i in range(10):
    list1.append(int(input(f'Digite o {i+1}° número da lista 1: ')))
    list2.append(int(input(f'Digite o {i+1}° número da lista 2: ')))

print(list1)
print(list2)
print(f'Listas intercaladas: {intercalated(list1, list2)}')