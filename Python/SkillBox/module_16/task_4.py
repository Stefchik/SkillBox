guests = ['Петя', 'Ваня', 'Саша', 'Лиза', 'Катя']
print(f'Сейчас на вечеринке {len(guests)} человек:', guests)

while True:
    question = input('Гость пришёл или ушёл? ')
    if question == 'Пора спать':
        break

    name_guest = input('Имя гостя: ')
    if question == 'ушел':
        guests.remove(name_guest)
        print(f'Пока, {name_guest}!')
        print(f'Сейчас на вечеринке {len(guests)} человек:', guests)

    if question == 'пришел':
        if len(guests) < 6:
            guests.append(name_guest)
            print(f'Привет, {name_guest}!')
            print(f'Сейчас на вечеринке {len(guests)} человек:', guests)
        else:
            print(f'Прости, {name_guest}, но мест нет.')
            print(f'Сейчас на вечеринке {len(guests)} человек:', guests)

print('Вечеринка закончилась, все легли спать.')
