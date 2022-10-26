def reversed_numbers(N):
    reverse_first = 0
    reverse_second = 0
    second_number = round(N - int(N), 2)
    first_number = N - second_number
    while first_number != 0:
        reverse_first = reverse_first * 10 + first_number % 10
        first_number //= 10
    second_number = 10 * round(N - int(N), 2)
    while second_number > 1:
        reverse_second = reverse_second * 10 + second_number % 1
        second_number = (second_number - reverse_second) * 0.01
        reverse_second += second_number
    return reverse_first + reverse_second
number_1 = float(input('Введите первое число: '))
number_2 = float(input('Введите второе число: '))
print('Первое число наоборот:', reversed_numbers(number_1))
print('Второе число наоборот:', reversed_numbers(number_2))
reverse_1 = reversed_numbers(number_1)
reverse_2 = reversed_numbers(number_2)
print('Сумма:', reverse_1 + reverse_2)

