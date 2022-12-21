import os

def file_sizes(path):
    files_stat = [0, 0, 0]

    for i_elem in os.listdir(path):
        if os.path.isfile(os.path.abspath(os.path.join(path, i_elem))):
            file_path = os.path.abspath(os.path.join(path, i_elem))
            file_size = os.path.getsize(file_path)
            files_stat[0] += file_size
            files_stat[1] += 1
        else:
            result = file_sizes(os.path.abspath(os.path.join(path, i_elem)))
            files_stat[0] += result[0]
            files_stat[1] += result[1]
            files_stat[2] += 1
    return files_stat

path = os.path.abspath(os.path.join('..', '..', 'Module22'))

result = file_sizes(path)
print(path)
print(f'Размер каталога (в Кб): {round(result[0] / 1024, 2):,}'.replace(',', ' '))
print(f'Количество файлов: {result[1]:,}'.replace(',', ' '))
print(f'Количество подкаталогов: {result[2]:,}'.replace(',', ' '))