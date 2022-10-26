def sum_numbers(N):
    numbers = 0
    while N != 0:
        numbers += (N % 10)
        N //= 10
    return numbers
def count_numbers(N):
    count = 0
    while N != 0:
        N //= 10
        count += 1
    return count
N = int(input('Введите число: '))
numbers = sum_numbers(N)
count = count_numbers(N)
print("Сумма чисел:", sum_numbers(N))
print("Количество цифр в числе:", count_numbers(N))
print('Разность суммы и количества цифр:', abs(numbers - count))
