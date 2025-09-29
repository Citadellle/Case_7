from bs4 import BeautifulSoup
import requests
import re


def search_url(url):
    '''
    function for searching all way's to goods in all page
    use libraries, like 're', 'requests', 'bs4'

    :param only url:
    :return all_goods list:
    '''

    #creating list for collecting ways to url page's
    all_goods = []
    r = requests.get(url)
    soup = BeautifulSoup(r.text, "html.parser")

    #creating list product names url of this product inside
    info = soup.findAll(class_='gr-product-name')

    #for cycle for appending urls in 'all_goods' list
    for data in info:
        if data is not None:
            href = re.findall(r'href="([^"]*)"', str(data))
            all_goods.append(href)
    print(all_goods)
    return all_goods


search_url(r'https://obuv-tut2000.ru/magazin/search?p=2&gr_smart_search=1&search_text=37&s[sort_by]=price%20asc')
