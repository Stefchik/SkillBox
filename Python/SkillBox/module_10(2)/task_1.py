def check_len(string):
    if len(string) < 3:
        raise Exception('Ошибка: Менее трёх символов в строке {}.'.format(line_number))
    return True

def load_data(file_name, charset='utf-8'):
    global people_data
    with open(file_name, 'r', encoding=charset) as data_file:
        for line in data_file:
            people_data.append(line.strip())
    print(people_data)

line_number = 0
symbol_count = 0
people_data = []

load_data('people.txt')

for line in people_data:
    line_number += 1
    try:
        if check_len(line):
            symbol_count += len(line)
    except Exception as ex:
        print(ex)

print('Общее количество символов:', symbol_count)
