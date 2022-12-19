data_set = {}
count_country = int(input('Кол-во стран: '))

for i in range(count_country):
    value = input('{} страна: '.format(i + 1)).split()
    for city in value[1:]:
        data_set[city] = value[0]

for i in range(3):
    city = input('\n{} город: '.format(i + 1))
    country = data_set.get(city)
    if country:
        print(f'Город {city} расположен в стране {country}.')
    else:
        print(f'По городу {city} данных нет.')