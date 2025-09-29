from bs4 import BeautifulSoup
import requests
import re


def search_url(url):
    all_goods = {}
    r = requests.get(url)
    soup = BeautifulSoup(r.text, "html.parser")
    info = soup.findAll(class_='gr-product-name')

    for data in info:
        if data is not None:
            href = re.findall(r'href="([^"]*)"', str(data))
            good = re.findall(r'>(.*)</a>', str(data))
            all_goods[*good] = href
    print(all_goods)
    return all_goods


search_url(r'https://obuv-tut2000.ru/magazin/search?p=2&gr_smart_search=1&search_text=37&s[sort_by]=price%20asc')