import pandas as pd
from bs4 import BeautifulSoup
from request_site import request_to_site
from time_convey import convet_time

import numpy as np

#Парсим yandex новости по региону
url_main = 'https://news.yandex.ru/Moscow_and_Moscow_Oblast/index.html'


def parse_news(url):
    html_doc = request_to_site(url)
    soup = BeautifulSoup(html_doc, 'html.parser')
    yan_dom = 'https://yandex.ru'

    try:
        title_news = soup.findAll('h2', {'class': 'story__title'})  # заголовок и ссылка на новость
        newsdates = soup.find_all('div', attrs={'class': 'story__date'})  # текст, где есть дата

    except AttributeError:
        print("Нет данных")

    # список заголовков
    title_list = [x.find('a').string for x in title_news]

    # выбираем ссылки
    link_list = [x.find('a')['href'] for x in title_news]
    link_list_1 = [] #добавляем домен, где его нет
    for x in link_list:
        if x[:17] != yan_dom:
            new_link = yan_dom + x
            link_list_1.append(new_link)
        else:
            link_list_1.append(x)

    # Парсим текст каждой новости по полученному ссылке
    body_texts = []
    for url in link_list_1:
        html_doc = request_to_site(url)
        soup = BeautifulSoup(html_doc, 'html.parser')
        news_body = soup.findAll('div', {'class': 'doc__text'})
        body_texts.append(news_body[0].text)

    # ищем время и форматируем его
    date_list = [x.text for x in newsdates]
    date_list_format = convet_time(date_list)

    # делаем dataframe
    columns = ['title', 'date', 'newsbody', 'link']
    df = pd.DataFrame(list(zip(title_list, date_list_format, body_texts, link_list_1)), columns=columns)
    df.index = np.arange(1, len(df) + 1)  # увеличиваем индекс на 1, чтобы он не начинался с 0
    df.index.name = 'id'  # присваиваем индексу имя
    return df.sort_values(by=['date'], ascending=False)
