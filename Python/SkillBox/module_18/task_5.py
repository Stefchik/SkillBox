while True:
    password = input('Придумайте пароль: ')
    password_length = len(password)
    password_upper = sum(map(str.isupper, password))
    password_numbers = sum(map(str.isdigit, password))

    if (password_length < 8) or (password_upper < 1) or (password_numbers < 3):
        print('Пароль ненадёжный. Попробуйте ещё раз.')
    else:
        print('Это надёжный пароль!')
        break