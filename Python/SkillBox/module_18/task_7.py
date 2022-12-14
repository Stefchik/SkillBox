ip = input('Введите IP: ').split('.')

if len(ip) < 4:
    print('Адрес - это четыре числа, разделённые точками')
else:
    count_numbers = 0
    out_of_range = 0
    for x in ip:
        if x.isdigit():
            count_numbers += 1
            if int(x) > 255:
                out_of_range += 1
                print(x, 'превышает 255')
        else:
            print(x, '- не целое число')
    if out_of_range == 0 and count_numbers == 4:
        print('IP-адрес корректен')