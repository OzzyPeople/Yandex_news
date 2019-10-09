import datetime
import re

def convet_time(time_text):

    today_date = datetime.datetime.today()
    yesterday_date = datetime.datetime.now() - datetime.timedelta(days=1)
    list_months = ['start', 'января', 'февраля','марта', 'апреля', 'мая', 'июня', 'июля', 'августа', 'сентября', 'октября', 'ноября', 'декабря']
    list_dates_1 = []
    for text in time_text:
            #есть ли упоминание месяца в тексте
            month_x = [ele for ele in list_months if(ele in text)]
            #если новость за вчерашний день
            if 'вчера' in time_text:
                list_dates_1.append(yesterday_date.strftime("%Y/%m/%d"))
            #не сегодня и не вчера
            elif len(month_x) > 0:
                se = re.search(r'(\d){2}', text) #ищем первые две цифры через регулярные выражения
                datum = f'{today_date.year}/{list_months.index(month_x[0])}/{se[0]}'
                list_dates_1.append(datum)
            #сегодня
            elif len(month_x)==0:
                list_dates_1.append(today_date.strftime("%Y/%m/%d"))
    return list_dates_1