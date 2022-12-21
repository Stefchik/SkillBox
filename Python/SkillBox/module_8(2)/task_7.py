def summ(*args):
    def flatten(a_list):
        result = []
        for e in a_list:
            if isinstance(e, int):
                result.append(e)
            else:
                result.extend(flatten(e))
        return result

    return sum(flatten(args))


result = summ([[1, 2, [3]], [1], 3])
print('Ответ:', result)
result = summ(1, 2, 3, 4, 5)
print('Ответ:', result)
