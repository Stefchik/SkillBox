shop = [['каретка', 1200], ['шатун', 1000], ['седло', 300],
        ['педаль', 100], ['седло', 1500], ['рама', 12000],
        ['обод', 2000], ['шатун', 200], ['седло', 2700]]

count = 0
cost = 0
name_detail = input('Название детали: ')

for i_elem in range(len(shop)):
    if shop[i_elem][0] == name_detail.lower():
        count += 1
        cost += shop[i_elem][1]
print()
if count > 0:
    print('Кол-во деталей -', count)
    print('Общая стоимость -', cost)
else:
    print('Товар не найден.')
