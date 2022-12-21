count = 0
tmp_str = ''

with open('numbers.txt') as file:
    for row in file.readlines():
        tmp_str = row.strip()
        if tmp_str != '':
            count += int(tmp_str)

f = open('answer.txt', 'w')
f.write(str(count))
f.close()
