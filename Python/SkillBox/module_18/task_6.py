text = input('Введите строку: ')
str_len = len(text)
result = ''
if str_len > 0:
    i = 0
    while i < str_len:
        counter = 0
        curr_char = text[i:i + 1]
        while i < str_len and text[i] == curr_char:
            i += 1
            counter += 1
        result += curr_char + str(counter)
print(result)