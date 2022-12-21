import os
import string

f = open(os.path.join('..', '02_zen_of_python', 'zen.txt'))
line_count = 0
word_count = 0
symbol_count = 0
symbol_dict = {}

for i in f:
    line_count += 1

    sym_row = i.strip()
    for sym in string.punctuation:
        sym_row = sym_row.replace(sym, '')
    sym_row = sym_row.replace(' ', '')
    symbol_count += len(sym_row)

    word_count += len(i.split())

    sd = {}
    row_lower = i.lower()
    for s in row_lower:
        if s in string.ascii_lowercase:
            sd[s] = row_lower.count(s)
    # print('sd', sd)
    for k, v in sd.items():
        if k in symbol_dict:
            symbol_dict[k] += v
        else:
            symbol_dict[k] = v

f.close()

print('Количество букв в файле:', symbol_count)
print('Количество слов в файле:', word_count)
print('Количество строк в файле:', line_count)

letter_min = sorted(symbol_dict.items(), key=lambda x: x[1], reverse=False)[0][0]
print('Наиболее редкая буква:', letter_min, symbol_dict[letter_min])

letter_max = sorted(symbol_dict.items(), key=lambda x: x[1], reverse=True)[0][0]
print('Наиболее частая буква:', letter_max, symbol_dict[letter_max])
