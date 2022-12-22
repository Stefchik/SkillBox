import time
import random
import requests


def slow_down(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        time.sleep(random.randint(1, 5))
        return_value = func(*args, **kwargs)
        end = time.time()
        print('[*] Время выполнения: {} секунд.'.format(end - start))
        return return_value

    return wrapper

@slow_down
def get_webpage(page: str) -> str:
    response: requests
    print(f'Получение данных со страницы: {page}')
    try:
        response = requests.get(page, timeout=5)
        print('Данные успешно получены')
        result = response.text
        response.close()
    except requests.exceptions.RequestException as err:
        result = err
    return result

page_one = get_webpage('https://google.com')
page_two = get_webpage('https://yandex.ru')
page_three = get_webpage('https://1111.ru')
