count_word = int(input('Введите количество пар слов: '))
text_dict = dict()

for i in range(1, count_word + 1):
    text = input(f'{i} пара: ').lower().split('-')
    text_dict[text[0].strip()] = text[1].strip()
    text_dict[text[1].strip()] = text[0].strip()

while True:
    word = input('\nВведите слово: ').lower().strip()
    if word == 'end':
        break
    elif word in text_dict:
        print('Синоним:', text_dict[word])
    else:
        print('Такого слова в словаре нет.')