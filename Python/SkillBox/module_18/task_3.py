name_file = input('Название файла: ')
special_sym = ('@', '№', '$', '%', '^', '&', '*')
file_extension = ('.txt', '.docx')
if name_file.startswith(special_sym):
    print('Ошибка: название начинается на один из специальных символов.')
elif not name_file.endswith(file_extension):
    print('Ошибка: неверное расширение файла. Ожидалось .txt или .docx.')
else:
    print('Файл назван верно.')