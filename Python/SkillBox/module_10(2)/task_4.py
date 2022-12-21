import re
import os

def check_email(email):
    return re.fullmatch(regex, email)

def check_valid(data):
    arr = data.split()
    if len(arr) < 3:
        raise IndexError('НЕ присутствуют все три поля')
    else:
        if not arr[0].isalpha():
            raise NameError('Поле «Имя» содержит НЕ только буквы')
        if not check_email(arr[1]):
            raise SyntaxError('Поле «Имейл» НЕ содержит @ и . (точку)')
        if not arr[2].isdigit():
            raise ValueError('Поле «Возраст» НЕ является числом')
        elif int(arr[2]) < 10 or int(arr[2]) > 100:
            raise ValueError('Поле «Возраст» НЕ является числом от 10 до 99')
    return True

FILE_REG = 'registrations.txt'
FILE_GOOD = 'registrations_good.log'
FILE_BAD = 'registrations_bad.log'
regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
row_number = 0

try:
    os.remove(FILE_GOOD)
    os.remove(FILE_BAD)
except OSError as e:
    print(e)

with open(FILE_REG, 'r', encoding='utf8') as f_reg, \
        open(FILE_GOOD, 'a', encoding='utf8') as f_good, \
        open(FILE_BAD, 'a', encoding='utf8') as f_bad:
    for line in f_reg:
        row_number += 1
        try:
            if line != '\n':
                if check_valid(line):
                    f_good.write(line)
        except (IndexError, NameError, SyntaxError, ValueError) as err:
            error_message = f'{line.rstrip()} - {err.__class__.__name__} - {err}\n'
            f_bad.write(error_message)