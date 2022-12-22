import re

phone_list = ['9999999999', '999999-999', '99999x9999', '+79261234567', '89261234567', '79261234567',
              '+7 926 123 45 67', '8(926)123-45-67', '123-45-67', '9261234567', '79261234567', '(495)1234567',
              '(495) 123 45 67', '89261234567', '8-926-123-45-67', '8 927 1234 234', '8 927 12 12 888',
              '8 927 12 555 12', '8 927 123 8 123']

pattern = r'^((8|\+7)[\- ]?)?(\(?\d{3}\)?[\- ]?)?[\d\- ]{7,10}$'

def clean_up_number(phone_number: str, print_debug: bool = False) -> str:
    """
    Отчистим номер от лишних символов
    :param phone_number: Телефонный номер
    :param print_debug: Нужно ли выводить результат отчистки
    :return: Возвращаем чистый номер
    """

    removed_chars = [' ', '(', ')', '+', '-', '.', ',', '!']
    clear_number = ''.join(filter(lambda x: x not in removed_chars, phone_number))
    if print_debug:
        print(f'🔁 Грязный номер: {phone_number} Чистый номер: {clear_number}')
    return clear_number

def check_phone_number(phone_number: str, check_length: bool = True, min_length: int = 10, pattern: str = None) -> bool:
    """
    Проверяем номер телефона на валидность
    :param phone_number: Телефонный номер
    :param check_length: Проверять длину номера
    :param min_length: Минимальная длинная номера
    :param pattern: Паттерн для проверки
    :return: bool
    """

    if check_length:
        if len(phone_number) < min_length:
            return False

    if pattern is None:
        pat = r'^((8|\+7)[\- ]?)?(\(?\d{3}\)?[\- ]?)?[\d\- ]{7,10}$'
    else:
        pat = pattern

    if re.search(pat, phone_number):
        return True
    else:
        return False

def check_number(phone_number: str, pattern: str) -> bool:
    """
    Вариант 2. Более короткий
    :param phone_number: Телефонный номер
    :param pattern: Паттерн для проверки
    :return:
    """

    if re.match(pattern, phone_number) and len(phone_number) == 10:
        return True
    else:
        return False

if __name__ == '__main__':
    counter = 0
    for item in phone_list:
        counter += 1
        res = 'всё в порядке' if check_phone_number(clean_up_number(item, True)) else 'не подходит'
        print(f'{counter} номер {item}: {res}')

    print('*' * 40 + '\n')
    counter = 0
    for item in phone_list:
        counter += 1
        res = 'всё в порядке' if check_number(clean_up_number(item), pattern) else 'не подходит'
        print(f'{counter} номер {item}: {res}')

    print('*' * 40 + '\n')
    counter = 0
    for item in phone_list:
        counter += 1
        res1 = 'всё в порядке' if check_phone_number(clean_up_number(item)) else 'не подходит'
        res2 = 'всё в порядке' if check_number(clean_up_number(item), pattern) else 'не подходит'
        print(f'{counter} номер {item}: {res1} - {res2}')
