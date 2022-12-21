import os

text = input('Введите строку: ')
print('Куда хотите сохранить документ? Введите последовательность папок (через пробел):')
folder = input().replace(' ', os.path.sep)
file_name = input('Введите имя файла: ')
if not file_name.endswith('.txt'):
    file_name += '.txt'
print(file_name)

path = os.path.join(os.path.sep, folder, file_name)
check_file = os.path.exists(path)

if check_file:
    answer = input('Вы действительно хотите перезаписать файл (Да/Нет)? ').lower()
    if answer == 'да' or answer == 'yes':
        with open(file_name, 'w') as file_object:
            file_object.write(text)
            file_object.close()
            print('Файл успешно перезаписан!')
    else:
        print('Вы отказались от перезаписи файла.')
else:
    with open(file_name, 'w') as file_object:
        file_object.write(text)
        file_object.close()
        print('Файл успешно сохранён!')
