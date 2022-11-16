word = input('Введите слово: ')
symbol_list = list(word)
unique_symbols = 0
for letter in symbol_list:
    count = 0
    for i in symbol_list:
        if letter == i:
            count+=1
    if count == 1:
        unique_symbols += 1
print('Количество уникальных букв:', unique_symbols)