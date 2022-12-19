max_numbers = int(input('Введите максимальное число: '))
all_nums = set(range(1, max_numbers + 1))
while True:
    right_number = input('Нужное число есть среди вот этих чисел: ')
    if right_number == 'Помогите!':
        break
    right_number = {int(x) for x in right_number.split()}
    answer = input('Ответ Артёма: ')
    if answer == 'Да':
        all_nums &= right_number
    else:
        all_nums -= right_number

print(*all_nums)