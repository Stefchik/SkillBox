def search(data_dict, find_key, depth=-1):
    if depth == -1:
        res = []
        for k in data_dict.keys():
            if k == find_key:
                res = res + [data_dict[k]]
            if type(data_dict[k]) is dict:
                res = res + search(data_dict[k], find_key, depth=-1)
        return res
    else:
        if depth == 0:
            return []
        else:
            res = []
            for k in data_dict.keys():
                if k == find_key:
                    res = res + [data_dict[k]]
                if type(data_dict[k]) is dict:
                    res = res + search(data_dict[k], find_key, depth - 1)
            return res


def ask_yn():
    result = -1
    choice = input('Хотите ввести максимальную глубину? Y/N: ').lower()
    if choice == 'y':
        result = int(input('Введите максимальную глубину: '))
    return result


site = {
    'html': {
        'head': {
            'title': 'Мой сайт'
        },
        'body': {
            'h2': 'Здесь будет мой заголовок',
            'div': 'Тут, наверное, какой-то блок',
            'p': 'А вот здесь новый абзац'
        }
    }
}

find_key = input('Введите искомый ключ: ')
depth = ask_yn()

if depth > 0:
    result = search(site, find_key, depth)
else:
    result = search(site, find_key)

print('Значение ключа:', result)

def find_key(struct, key, max_depth=None, depth=1):
    result = None

    if max_depth and max_depth < depth:
        return result

    if key in struct:
        return struct[key]

    for sub_struct in struct.values():

        if isinstance(sub_struct, dict):

            result = find_key(sub_struct, key, max_depth, depth=depth + 1)

            if result:
                break

    return result

site = {
    'html': {
        'head': {
            'title': 'Мой сайт'
        },
        'body': {
            'h2': 'Здесь будет мой заголовок',
            'div': 'Тут, наверное, какой-то блок',
            'p': 'А вот здесь новый абзац'
        }
    }
}

key = input('Введите искомый ключ: ')
answer = input('Хотите ввести максимальную глубину? Y/N: ')
if answer.lower() == 'y':
    max_depth = int(input('Введите максимальную глубину: '))
else:
    max_depth = None

print('Значение ключа:', find_key(struct=site, max_depth=max_depth, key=key))
