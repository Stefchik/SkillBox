count_orders = int(input('Введите кол-во заказов: '))
orders_data = {}

for i in range(1, count_orders + 1):
    order = input(f'{i} заказ: ')
    fio, name_pizza, numbers_pizza = order.rsplit(maxsplit=3)
    numbers_pizza = int(numbers_pizza)
    if fio not in orders_data:
        orders_data[fio] = {name_pizza: numbers_pizza}
    else:
        if name_pizza not in orders_data[fio]:
            orders_data[fio][name_pizza] = numbers_pizza
        else:
            orders_data[fio][name_pizza] += numbers_pizza

for fio, order in sorted(orders_data.items()):
    print(f'{fio}:')
    for name_pizza, numbers_pizza in sorted(order.items()):
        print('\t', name_pizza, numbers_pizza)