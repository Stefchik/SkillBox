number = int(input('Введите целое число: '))
new_list = []
for i in range(number + 1):
    if i % 2 == 1:
        new_list.append(i)
print('Список из нечётных чисел от одного до N:', new_list)