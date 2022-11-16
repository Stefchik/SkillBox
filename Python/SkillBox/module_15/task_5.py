films = ['Крепкий орешек', 'Назад в будущее', 'Таксист', 'Леон', 'Город грехов', 'Мементо']
favorite_films = []
count_film = int(input('Сколько фильмов хотите добавить? '))
flag = True
for _ in range(count_film):
    name_film = input('Введите название фильма: ')
    for film in films:
        if film == name_film:
            flag = True
            favorite_films.append(film)
            break
        else:
            flag = False
    if flag is False:
        print(f'Ошибка: фильма {name_film} у нас нет :(')
print(favorite_films)