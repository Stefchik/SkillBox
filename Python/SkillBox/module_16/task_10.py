count_number = int(input('Кол-во чисел: '))
arr = []

for i in range(count_number):
    arr.append(int(input('Число: ')))

counter = 0
while arr != arr[::-1]:
    arr.insert(count_number, arr[counter])
    counter += 1

print('Нужно приписать чисел:', counter)
print('Сами числа:', *arr[:counter][::-1])