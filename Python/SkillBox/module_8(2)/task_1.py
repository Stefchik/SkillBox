def print_to(end, start=1):
    if start <= end:
        print(start)
        print_to(end, start + 1)

print_to(int(input('Введите num: ')))
