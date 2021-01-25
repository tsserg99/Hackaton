import requests
import lxml.html
from flask import Flask, render_template
from bs4 import BeautifulSoup

# url_roz = "https://rozetka.com.ua/ua/krupy/c4628397/"
# api = requests.get(url_roz)
# tree = lxml.html.document_fromstring(api.text)
# text = tree.xpath(
#     '/html/body/app-root/div/div[1]/rz-category/div/main/rz-catalog/div/div/section/rz-grid/ul/li[2]/app-goods-tile-default/div/div[2]/div[4]/div[2]/p/span[1]/text()')
# # for i in range(len(text)):
# #     print('Гречка 1кг на "Rozetka":'+str(text[i])+"грн.")
#
#
# url_agro = "https://agro-ukraine.com/ru/trade/rf-137/p-1/"
# api_2 = requests.get(url_agro)
# tree_2 = lxml.html.document_fromstring(api_2.text)
# text_2 = tree_2.xpath('//*[@id="605171"]/div[1]/div[2]/span/text()')
# # for i in range(len(text_2)):
# #     print('Гречка 1кг на "Agro-Ukraine":', str(text_2[i]))
#
# url_fozzy = "https://fozzyshop.ua/ru/300143-krupa-grechnevaya"
# api_3 = requests.get(url_fozzy)
# tree_3 = lxml.html.document_fromstring(api_3.text)
# text_3 = tree_3.xpath('//*[@id="js-product-list"]/div/div[1]/article/div[2]/div[6]/a/span/text()')
# # for i in range(len(text_3)):
# #     print('Гречка 1кг на "FOZZY shop":', str(text_3[i]) + ".")
#

app = Flask(__name__)

url = 'https://rozetka.com.ua/ua/krupy/c4628397/vid-225787=grechka/'
url_2 = 'https://agro-ukraine.com/ru/trade/?adv_search=1&lang=ru&form_mode=1&q=%D0%B3%D1%80%D0%B5%D1%87%D0%B0%D0%BD%D0%B0++%7C+%D0%B3%D1%80%D0%B5%D1%87%D0%BD%D0%B5%D0%B2%D0%B0%D1%8F&rgn_id=0&rgn_id_all_sub=0&r_id=59&r_id_all_sub=0&types_id=2&price_from=1&price_to=&price_currency_id=2&sort_mode=3'
url_3 = 'https://fozzyshop.ua/ru/300143-krupa-grechnevaya/s-15/kategoriya-krupa_grechnevaya'

response = requests.get(url)
response_2 = requests.get(url_2)
response_3 = requests.get(url_3)

soup = BeautifulSoup(response.text, 'lxml')
quotes = soup.find_all('span', class_='goods-tile__title')
price = soup.find_all('span', class_='goods-tile__price-value')

soup_2 = BeautifulSoup(response_2.text, 'lxml')
quotes_2 = soup_2.find_all('a', class_='i_title ff2')
price_2 = soup_2.find_all('span', class_='i_price')

soup_3 = BeautifulSoup(response_3.text, 'lxml')
quotes_3 = soup_3.find_all('div', class_='h3 product-title')
price_3 = soup_3.find_all('span', class_='product-price')


@app.route("/index")
def index():
    return render_template('index.html')

@app.route("/rozetka")
def roz():
    length_1 = {'len': len(quotes)}

    def run():
        li = []
        pr = []

        for i in range(len(quotes)):
            li.append(quotes[i].text)
            pr.append(price[i].text + ' - грн')
            r = {'username': li, 'price': pr, 'space': ' \n'}
        return r

    return render_template('rozetka.html', r=run(), l1=length_1)

@app.route("/agro")
def agr():
    length_1 = {'len': len(quotes)}

    def run():
        li = []
        pr = []

        for i in range(len(quotes_2[:16])):
            li.append(quotes_2[i].text)
            pr.append(price_2[i].text + ' - грн')
            r = {'username': li, 'price': pr, 'space': ' \n'}
        return r

    return render_template('agro.html', r=run(), l1=length_1)

@app.route("/fozzy")
def foz():
    length_1 = {'len': len(quotes)}

    def run():
        li = []
        pr = []

        for i in range(len(quotes_3)):
            li.append(quotes_3[i].text)
            pr.append(price_3[i].text + ' - грн')
            r = {'username': li, 'price': pr, 'space': ' \n'}
        return r

    return render_template('agro.html', r=run(), l1=length_1)

if __name__ == "__main__":
    app.run(debug=True, port=5000, host=0000)
