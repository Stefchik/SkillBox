count_videocards = int(input('Количество видеокарт: '))
list = []
maxx = 0
for i in range(1, count_videocards + 1):
    videocard = int(input(f'{i} Видеокарта: '))
    list.append(videocard)
print('Старый список видеокарт:', list)
list.remove(max(list))
print('Новый список видеокарт:', list)
