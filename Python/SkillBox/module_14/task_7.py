def three_numbers(years_1, years_2):
    for i in range(years_1, years_2 + 1):
        a = i // 1000
        b = i // 100 % 10
        c = i // 10 % 10
        d = i % 10
        if a == b == c or b == c == d:
            print(i)
years_1 = int(input('Введите первый год: '))
years_2 = int(input('Введите второй год: '))
print(f'Года от {years_1} до {years_2} с тремя одинаковыми цифрами:')
three_numbers(years_1, years_2)