shift = int(input('Сдвиг: '))
list = input('Изначальный список: ').split()
print('Изначальный список:', list)
for i in range(shift):
    list = [list[-1]] + list
    list.pop(5)
print('Сдвинутый спискок:', list)