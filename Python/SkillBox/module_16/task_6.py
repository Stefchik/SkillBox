list_1 = []
list_2 = []

for i_elem in range(3):
    query = 'Введите ' + str(i_elem + 1) + ' число для первого списка: '
    number = int(input(query))
    list_1.append(number)

for i_elem in range(7):
    query = 'Введите ' + str(i_elem + 1) + ' число для второго списка: '
    number = int(input(query))
    list_2.append(number)

list_1.extend(list_2)
for _ in range(len(list_1)):
    for i_elem in list_1:
        if list_1.count(i_elem) > 1:
            list_1.remove(i_elem)

print(list_1)