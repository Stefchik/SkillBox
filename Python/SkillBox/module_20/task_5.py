d = {
    'Сидоров Никита': 35,
    'Сидорова Алина': 34,
    'Сидоров Павел': 10,
    'Петров Виктор': 15,
    'Петрова Дарья': 16
}
ending = {'ов': 'ова', 'ев': 'ева', 'ий': 'ая', 'ин': 'ина'}


def last_char(in_str):
    for key, value in ending.items():
        if in_str.endswith(key):
            in_str = in_str[0:-len(key)]
            break
        if in_str.endswith(value):
            in_str = in_str[0:-len(value)]
            break
    return in_str


search = input('Введите фамилию: ').lower()
search_part = last_char(search)
result = []

for i in d:
    if search_part in i.split()[0].lower():
        result.append(i + ' ' + str(d[i]))

if not result:
    print('Поиск не дал результатов')
else:
    for i in result:
        print(i)
