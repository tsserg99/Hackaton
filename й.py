import requests
from bs4 import BeautifulSoup
import json
import itertools

url = 'https://rozetka.com.ua/ua/krupy/c4628397/vid-225787=grechka/'
url_2 = 'https://agro-ukraine.com/ru/trade/?adv_search=1&lang=ru&form_mode=1&q=%D0%B3%D1%80%D0%B5%D1%87%D0%B0%D0%BD%D0%B0++%7C+%D0%B3%D1%80%D0%B5%D1%87%D0%BD%D0%B5%D0%B2%D0%B0%D1%8F&rgn_id=0&rgn_id_all_sub=0&r_id=59&r_id_all_sub=0&types_id=2&price_from=1&price_to=&price_currency_id=2&sort_mode=3'
url_3 = 'https://fozzyshop.ua/ru/300143-krupa-grechnevaya/s-15/kategoriya-krupa_grechnevaya'

response = requests.get(url)
response_2 = requests.get(url_2)
response_3 = requests.get(url_3)

soup = BeautifulSoup(response.text, 'lxml')
quotes = soup.find_all('span', class_='goods-tile__title')
price = soup.find_all('span', class_='goods-tile__price-value')


li = []
pr = []
ss = []
#
# for i in range(len(quotes)):
#     li = quotes[i].text
#     pr = price[i].text
#     uan = 'грн'
#     col = li + pr + uan
#     print(count)

    # for i in range(len(quotes)):
    #     li = quotes[i].text
    #     pr = price[i].text
    #     uan = 'грн'
    #     col_1 = li + pr + uan
    #     print(type(col_1))
    # #   print(len(col_1))

for i in range(len(quotes)):
    li.append(quotes[i].text)
    pr.append(price[i].text)
    ss = list(zip(li, pr))

print(ss)
print(type(ss))
# print('\n'.join(ss))

# soup_2 = BeautifulSoup(response_2.text, 'lxml')
# quotes_2 = soup_2.find_all('a', class_='i_title ff2')
# price_2 = soup_2.find_all('span', class_='i_price')
#
#
# soup_3 = BeautifulSoup(response_3.text, 'lxml')
# quotes_3 = soup_3.find_all('div', class_='h3 product-title')
# price_3 = soup_3.find_all('span', class_='product-price')

# def roz():
#     print("=============Rozetka==============")
#     for i in range(0, len(quotes)):
#         print(quotes[i].text + '-' + price[i].text + 'грн')
#
# def agr():
#     print("=============Agr==============")
#     for i in range(0, len(quotes_2[:16])):
#         print(quotes_2[i].text + '-' + price_2[i].text)
#
# def fozz():
#     print("=============Fozzy==============")
#     for i in range(0, len(quotes_3)):
#         print(quotes_3[i].text + '-' + price_3[i].text)

# roz()
# agr()
# fozz()



#
# for tag in (price):
#     pri = tag.text.strip()
#     print(pri, file=fw, sep="\n")