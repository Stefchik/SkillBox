friend = int(input('Кол-во друзей: '))
receipt = int(input('Долговых расписок: '))
friends_list = []

for _ in range(friend):
    friends_list.append(0)

for i_elem in range(receipt):
    print(f'\n{i_elem + 1} расписка')
    to_who = int(input('Кому: '))
    from_who = int(input('От кого: '))
    how_much = int(input('Сколько: '))
    friends_list[from_who - 1] += how_much
    friends_list[to_who - 1] -= how_much

print('\nБаланс друзей:')
for index in range(len(friends_list)):
    print(f'{index + 1} : {friends_list[index]}')