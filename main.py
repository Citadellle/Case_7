import requests
from bs4 import BeautifulSoup
from tqdm import tqdm
from ru_local import *
from const import *


def search_urls_pages():
    """
    creates a list containing links to all the necessary product pages
    use libraries, like 'requests', 'bs4', 'const'

    :return url_list:
    """
    link4 = input()

    url_list = []
    url = fr'{LINK1}0{LINK3}{link4}'

    r = requests.get(url)   
    soup = BeautifulSoup(r.text, 'html.parser')
    max_num_page = int(soup.find(class_='page-num page_last').text)

    for link2 in range(max_num_page):
        url = fr'{LINK1}{link2}{LINK3}{link4}'
        url_list.append(url)

    return url_list


def search_urls_goods(url):
    '''
    function for searching all way's to goods in all page
    use libraries, like 'requests', 'bs4'

    :param only url:
    :return urls list:
    '''

    #creating list for collecting ways to url page's
    urls = []
    r = requests.get(url)
    soup = BeautifulSoup(r.text, "html.parser")

    info = soup.find_all(class_='gr-product-name')
    for i in info:
        urls.append(i.find('a').get('href'))
    
    return urls



def product_data(url):
    """
    function for searching information of product
    use libraries, like 'requests', 'bs4'

    :param only url:
    :return dict:
    """
    
    page = requests.get(url)
    bs = BeautifulSoup(page.text, 'html.parser')

    keys = [ARTICLE, NAME, VIEW,
            SEASON, PRICE, SIZES, UP_MATERIAL,
            COLOR, COUNTRY]
    data = dict.fromkeys(keys, '')

    data[ARTICLE] = bs.find(class_='shop2-product-article').find('span').next_sibling.strip()

    data[NAME] = bs.find(class_='gr-product-name').text.strip()

    try:
        data[VIEW] = bs.find(class_='shop2-product-params') \
            .find_all(class_='param-item even')[4] \
            .find(class_='param-body').text.strip()
    except:
        data[VIEW] = bs.find(class_='shop2-product-params') \
            .find_all(class_='param-item odd')[4] \
            .find(class_='param-body').text.strip()

    param_sezon = bs.find(class_='option-item sezon odd')
    if param_sezon is not None:
        data[SEASON] = param_sezon.find(class_='option-body').text.strip()
    else:
        data[SEASON] = bs.find(class_='option-item sezon even') \
            .find(class_='option-body').text.strip()

    data[PRICE] = bs.find(class_='product-price') \
        .find(class_='price-current').text.replace('\n', ' ').strip()

    param_size = bs.find(class_='option-item razmery_v_korobke even')
    if param_size is not None:
        data[SIZES] = param_size.find(class_='option-body').text.strip()
    else:
        data[SIZES] = bs.find(class_='option-item razmery_v_korobke odd') \
            .find(class_='option-body').text.strip()

    data[UP_MATERIAL] = bs.find(class_='option-item material_verha_960 odd') \
        .find(class_='option-body').text.strip()

    data[COLOR] = bs.find(class_='option-item cvet odd') \
        .find(class_='option-body').text.strip()

    param_country = bs.find(class_='gr-vendor-block')
    if param_country is not None:
        data[COUNTRY] = param_country.text.strip()
    else:
        pass

    return data


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


def main():
    '''
    main function
    '''
    urls_pages = search_urls_pages()

    urls_goods = []
    for url_page in tqdm(urls_pages):
        for url_product in search_urls_goods(url_page):
            urls_goods.append(url_product)
    
    goods_data = []
    for url in tqdm(urls_goods):
        print(LINK + url)
        goods_data.append(product_data(LINK + url))
    
    for i in goods_data:
        print(i)
    

if __name__ == '__main__':
    main()
