def score_key(a):
    return a[1][0] * 100000000 - a[1][1]

def check_len():
    global text, number_tuple
    result = 0
    len_range = len(text)
    len_turple = len(number_tuple)
    if len_range != len_turple:
        print('Данные имеют разную длину.')
        if len_range < len_turple:
            print('※ Кортеж будет урезан до длинны строки.')
            result = -1
        else:
            print('※ Строка будет урезана до длинны кортежа.')
            result = 1
            len_range = len_turple
    return result, len_range

def gen_pair():
    global text, number_tuple, pair
    len_data = check_len()
    for i in range(len_data[1]):
        tmp_pair = (text[i], number_tuple[i])
        pair.append(tmp_pair)
    print(pair)

pair = []
text = input('Строка: ')
number = input('Кортеж чисел: ').replace('(', '').replace(')', '').replace(' ', '').split(',')
number_tuple = tuple(int(num) for num in number)

gen_pair()

score_table = {}
number_rows = int(input('Общее количество строк протокола: '))
print('Введите результат - имя участника (через пробел)')
for time in range(number_rows):
    ball, name = input(' {0} запись: '.format(time + 1)).split()
    ball = int(ball)
    if name in score_table:
        if ball > score_table[name][0]:
            score_table[name][0] = ball
            score_table[name][1] = time
    else:
        score_table[name] = [ball, time]
scores = list(score_table.items())

scores.sort(key=score_key, reverse=True)
print('\nИтоги соревнований:')
for winner_index in range(3):
    print(f' {winner_index + 1} место {scores[winner_index][0]} ', end=' ')
    print(f'({scores[winner_index][1][0]})', sep='')
