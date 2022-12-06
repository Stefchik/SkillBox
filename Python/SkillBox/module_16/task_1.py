main_list = [1, 5, 3]
side_list_1 = [1, 5, 1, 5]
side_list_2 = [1, 3, 1, 5, 3, 3]

main_list.extend(side_list_1)
count_number = main_list.count(5)
print('Кол-во цифр 5 при первом объединении:', count_number)

for _ in range(count_number):
    main_list.remove(5)

main_list.extend(side_list_2)
print('Кол-во цифр 3 при первом объединении:', main_list.count(3))
print(main_list)