from bs4 import BeautifulSoup
import requests


def link():
    LINK1 = 'https://obuv-tut2000.ru/magazin/search?p='
    LINK3 = '&gr_smart_search=1&s[sort_by]=price%20asc&search_text='
    link4 = input()

    url_list = []
    for link2 in range(500):
        url = fr'{LINK1}{link2}{LINK3}{link4}'
        url_list.append(url)

    return url_list
  
