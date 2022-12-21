import json
from copy import deepcopy

def find_key(struct, key, meaning):
    if key in struct:
        struct[key] = meaning
        return site

    for sub_struct in struct.values():
        if isinstance(sub_struct, dict):
            result = find_key(sub_struct, key, meaning)
            if result:
                return site

site = {
    'html': {
        'head': {
            'title': 'Куплю/продам телефон недорого'
        },
        'body': {
            'h2': 'У нас самая низкая цена на iphone',
            'div': 'Купить',
            'p': 'продать'
        }
    }
}
new_sites = []

number_sites = int(input('Сколько сайтов: '))
for num in range(number_sites):
    product_name = input('Введите название продукта для нового сайта: ')
    key = {'title': f'Куплю/продам {product_name} недорого', 'h2': f'У нас самая низкая цена на {product_name}'}
    tmp_site = deepcopy(site)
    for i in key:
        find_key(tmp_site, i, key[i])
    new_sites.append({product_name: tmp_site})

    for element in new_sites:
        for k, v in element.items():
            print(f'Сайт для {k}:')
            print('site = ', end='')
            print(json.dumps(v, indent=4, ensure_ascii=False))
