line_1 = input('Первая строка: ')
line_2 = input('Вторая строка: ')

if line_1 == line_2:
    print('Строки одинаковые.')
else:
    if len(line_1) != len(line_2):
        print('Строки имеют разную длину.')
    else:
        shift = 1
        flag = False
        for i in range(len(line_1) - 1):
            line_2 = line_2[-1] + line_2[:-1]
            if line_1 == line_2:
                print(f'Первая строка получается из второй со сдвигом {shift}.')
                flag = True
                break
            else:
                shift += 1
        if not flag:
            print('Первую строку нельзя получить из второй с помощью циклического сдвига.')
