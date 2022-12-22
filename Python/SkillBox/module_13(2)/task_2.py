import os
from typing import Union, List

def search_path(home: str, search: str) -> Union[bool, str]:
    for dirpath, dirnames, filenames in os.walk(home):
        for cur_dir in dirnames:
            if cur_dir == search:
                return os.path.join(dirpath, cur_dir)
    return False

def gen_files_path(home: str, search: str) -> List[str]:
    result = search_path(home, search)
    file_list = []
    if isinstance(result, str):
        with os.scandir(result) as files:
            for file_name in files:
                if not file_name.name.startswith('.') and file_name.is_file():
                    file_list.append(file_name.name)
    return file_list

print('\n'.join(gen_files_path('/home/lliammah/', 'Module26')))
