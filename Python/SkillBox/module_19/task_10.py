string = input('Введите строку: ').lower()
elements = set()

for word in string:
    if word in elements:
        elements.remove(word)
    else:
        elements.add(word)
print(('Можно', 'Нельзя')[len(elements) > 1], 'сделать полиндром')