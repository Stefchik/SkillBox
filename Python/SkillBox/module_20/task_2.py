def checking_array(checking_list):
    return [i for i, v in enumerate(checking_list) if is_prime(i)]

def is_prime(i_num):
    if i_num >= 2:
        result = True
        for i in range(2, i_num):
            if i_num % i == 0:
                result = False
                break
    else:
        result = False
    return result

def crypto(text):
    i_list = checking_array(text)
    elem = []
    for i_index in i_list:
        elem.append(text[i_index])
    return elem


print(crypto('О Дивный Новый мир!'))
print(crypto([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))
