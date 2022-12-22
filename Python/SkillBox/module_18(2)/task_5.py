import requests
import re

def get_html(url: str) -> str:
    try:
        r = requests.get(url).text
    except requests.exceptions.RequestException as err:
        r = err.message
    return r

def get_content(pattern: str, html: str) -> None:
    p = re.compile(pattern, re.IGNORECASE)
    res = re.findall(p, html)
    for e in res:
        print(e)

if __name__ == "__main__":
    pattern = r'<h3.*>(.+?)</h3>'

    """
    Изначально хотел выполнить задание с помощью пакета Beautiful Soup, но решил всё же
    ограничиться регулярками.
    """

    url = 'http://www.columbia.edu/~fdc/sample.html'
    html = get_html(url)
    # print(html)
    get_content(pattern, html)

    print('*' * 40)
    url = 'https://developer.mozilla.org/ru/docs/Web/HTML/Element/article'
    html = get_html(url)
    get_content(pattern, html)

    print('*' * 40)
    url = 'https://habr.com/ru/company/badoo/blog/343310/'
    html = get_html(url)
    get_content(pattern, html)
