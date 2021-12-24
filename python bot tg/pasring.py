import aiogram.utils.executor
import requests
from bs4 import BeautifulSoup as BS
def parsing():
    a = []
    r = requests.get("https://www.banki.ru/products/currency/cash/moskva/")
    html = BS(r.content, 'html.parser')
    for el in html.select(".font-bold"):
        currency = el.find('span')
        try:
            a.append(currency.get_text())
        except AttributeError:
            continue
    for el in html.select(".table-flex__th"):
        time = el.find('div', class_='text-align-center')
        try:
            a.append(time.get_text())
        except AttributeError:
            continue
    return a