phonebook = {}
menu = 'Введите номер действия:\n ▶ 1. Добавить контакт\n ▶ 2. Найти человека\n ▶ 0. Выход\n ▷ '

def check_contact(name):
    result = False
    if len(phonebook) > 0:
        for key, value in phonebook.items():
            c_first = str(key[0]).lower()
            c_last = str(key[1]).lower()
            if name[0].lower() == c_first:
                if name[1].lower() == c_last:
                    result = True
                    break
    return result

def add_contact():
    contact_name = input('Введите имя и фамилию нового контакта (через пробел): ').split()
    contact_number = input('Введите номер телефона: ')
    if not check_contact(contact_name):
        phonebook[tuple(contact_name)] = contact_number
    else:
        print('✘ Такой человек уже есть в контактах.')

def search_contact():
    if len(phonebook) > 0:
        last_name = input('Введите фамилию для поиска: ').lower()
        for key, value in phonebook.items():
            c_last = str(key[1]).lower()
            if last_name == c_last:
                print(*key, value)
                break
    else:
        print('◈ У нас пока нет ни одного контакта ◈')

while True:
    choice = input(menu)
    if not choice.isdigit():
        choice = 0
    else:
        choice = int(choice)
    if choice == 1:
        add_contact()
    elif choice == 2:
        search_contact()
    else:
        break
    print(' Текущий словарь контактов:', phonebook)
