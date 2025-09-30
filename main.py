from bs4 import BeautifulSoup
import requests


def link():
    LINK1 = 'https://obuv-tut2000.ru/magazin/search?p='
    LINK3 = '&gr_smart_search=1&s[sort_by]=price%20asc&search_text='
    link4 = input()

    url_list = []
    url = fr'{LINK1}0{LINK3}{link4}'
    r = requests.get(url)
    soup = BeautifulSoup(r.text, 'html.parser')
    soup = soup.find('li', class_='page-num page_last').text
    for link2 in range(int(soup)):
        url = fr'{LINK1}{link2}{LINK3}{link4}'
        print(r.status_code)
        url_list.append(url)

    return url_list
