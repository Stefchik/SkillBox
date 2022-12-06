skates = []
people = []
count = 0

count_skates = int(input('Кол-во коньков: '))
for i_elem in range(count_skates):
    query = 'Размер ' + str(i_elem + 1) + '-й пары: '
    size_skates = int(input(query))
    skates.append(size_skates)

count_people = int(input('Кол-во людей: '))
for i_elem in range(count_people):
    query = 'Размер ноги ' + str(i_elem + 1) + '-й пары: '
    size_people = int(input(query))
    people.append(size_people)

for size in people:
    if size in skates:
        skates.remove(size)
        count += 1
print('Наибольшее кол-во людей, которые могут взять ролики:', count)
