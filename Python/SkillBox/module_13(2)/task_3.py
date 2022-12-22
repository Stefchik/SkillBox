import os
from typing import List, Union

def get_start_directory(home: str = None) -> Union[bool, str]:
    """
    Если директория не указана, то берём текущую.
    Если указанная директория не найдена, то берём текущую.

    :param home: str - Проверка директории
    """
    if home is None:
        return os.getcwd()
    if os.path.isdir(home):
        return home
    else:
        print('Указанная вами папка не найдена.')
        return False

def get_file_list(home: str) -> str:
    """
    Формирование списка файлов
    :param home: str - С какой директории начать
    """
    # r=root, d=directories, f = files
    for r, d, f in os.walk(home):
        for file in f:
            if file.endswith(".py"):
                yield os.path.join(r, file)

line_counter = 0
directory = get_start_directory('/home/lliammah/SkillBox/Python_Basic/Module26/')
if isinstance(directory, str):
    file_list = list(get_file_list(directory))
    if len(file_list) > 0:
        for file in file_list:
            try:
                cur_file = open(file, "r")
                local_count = 0
                for line in cur_file:
                    if line != '\n' or not line.startswith('"') or not line.startswith('#'):
                        local_count += 1
                print(f'{cur_file.name} - {local_count} строки')
                line_counter += local_count
                cur_file.close()
            except:
                continue
        print("=====================================")
        print("Всего строк  - ", line_counter)
