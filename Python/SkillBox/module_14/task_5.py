def min_divider(number):
    divider = 1
    for i in range(1, number + 1):
        if number % i == 0:
            divider = i
        if divider > 1:
            break
    return divider
number = int(input('Введите число: '))
print('Наименьший делитель, отличный от единицы:', min_divider(number))