def my_zip(*args: iter) -> tuple:
    count = 0
    args = list(map(list, args))
    while True:
        try:
            yield tuple(i[count] for i in args)
            count += 1
        except IndexError:
            break


a = [{'x': 4}, 'b', 'z', 'd']
b = (10, {20, }, [30], 'z')

result = my_zip(a, b)
for i_elem in result:
    print(i_elem)

a = [1, 2, 3, 4, 5]
b = {1: 's', 2: 'q', 3: 4}
x = (1, 2, 3, 4, 5)

result = my_zip(a, b, x)
for i_elem in result:
    print(i_elem)
