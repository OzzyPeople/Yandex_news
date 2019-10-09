import pymongo
from pymongo import MongoClient
from parse_news import parse_news

#Парсим yandex новости по региону
url = 'https://news.yandex.ru/Moscow_and_Moscow_Oblast/index.html'

def upload_mongodb(url):
    df = parse_news(url)
    client = MongoClient('mongodb://127.0.0.1:27017')
    db = client['news_parsing']
    news_parsing = db.news_parsing  # Имя коллекции
    df_dict = df.to_dict('records') #конвертируем dataframe в словарь
    news_parsing.insert_many(df_dict)
    print(news_parsing.count_documents({}))

upload_mongodb(url)