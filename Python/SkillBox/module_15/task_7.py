count_container = int(input('Кол-во контейнеров: '))
containers = []
row = 0
for i in range(count_container):
    while True:
        weight = int(input(f'Введите вес {i + 1} контейнера: '))
        if weight <= 200:
            break
    containers.append(weight)
containers.sort(reverse=True)
new_weight = int(input('Введите вес нового контейнера: '))
for i in range(len(containers)):
    row = i + 1
    if containers[i] < new_weight:
        break
print('Номер, который получит новый контейнер:', row)