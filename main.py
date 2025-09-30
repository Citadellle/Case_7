from bs4 import BeautifulSoup
import requests
from ru_local import *
from const import *


def link():
    """
    creates a list containing links to all the necessary product pages

    :return url_list:
    """
    
    link4 = input()

    url = fr'{LINK1}0{LINK3}{link4}'
    r = requests.get(url)
    soup = BeautifulSoup(r.text, 'html.parser')
    soup = soup.find('li', class_='page-num page_last').text

    url_list = []
    for link2 in range(int(soup)):
        url = fr'{LINK1}{link2}{LINK3}{link4}'
        url_list.append(url)

    return url_list


def output(goods_data):
    """
    the function displays product data in a separate file

    :param goods_data: contains a list of product information in the form of dictionaries
    :return:
    """
    
    with open('output.txt','w',encoding='utf-8') as catalog:
        for product in goods_data:
            catalog.write(INDENT)
            catalog.write(product[NAME])
            catalog.write(f'\n{ARTICLE}: {product[ARTICLE]}\n')
            catalog.write(f'{VIEW}: {product[VIEW]}\n')
            catalog.write(f'{SEASON}: {product[SEASON]}\n')
            catalog.write(f'{SIZES}: {product[SIZES]}\n')
            catalog.write(f'{PRICE}: {product[PRICE]}\n')
            catalog.write(f'{COLOR}: {product[COLOR]}\n')
            catalog.write(f'{UP_MATERIAL}: {product[UP_MATERIAL]}\n')
            catalog.write(f'{COUNTRY}: {product[COUNTRY]}\n')
