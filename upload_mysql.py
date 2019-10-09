import pymysql
import pandas
import sqlalchemy
from sqlalchemy import create_engine
from parse_news import parse_news
from change_data_type_mysql import change_data_type


if __name__ == '__main__':
    host = 'localhost'
    user = 'root'
    password = 'eBjjTk12551tSD'
    db_name = 'parsing'
    # Парсим yandex новости по региону
    url = 'https://news.yandex.ru/Moscow_and_Moscow_Oblast/index.html'

    df = parse_news(url)
    database_connection = sqlalchemy.create_engine('mysql+pymysql://{0}:{1}@{2}/{3}'.format(user, password, host, db_name))
    #создаем таблицу news_yandex в бд parsing
    df.to_sql(con=database_connection, name='news_yandex', if_exists='replace')
    print ('База данных загружена')

    change_data_type(host, user, password, db_name)
    print ('Формат данных изменен')