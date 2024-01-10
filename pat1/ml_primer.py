import pandas as pd
import numpy as np

"""задания решения"""

hotels = pd.read_csv('hotel_booking_data.csv') # отобразить таблицу
# hotels = len(hotels) # число строк в таблице
#hotels = hotels.isnull().sum() # проверка отсутствующих данних
#hotels = hotels.drop('company', axis=1) # удалить колонку
#hotels = hotels['country'].value_counts()[:5] # 5 часто встречающихся стран
#hotels = hotels.sort_values('adr', ascending=False)[['adr', 'name']].iloc[0] # найти клиента кто заб=платим макс. сумм.
#hotels = round(hotels['adr'].mean(), 2) # средняя цена номера с округлением до 2 знаков.
#hotels['total_stay_nights'] = hotels['stays_in_week_nights'] + hotels['stays_in_weekend_nights']
#hotels = round(hotels['total_stay_nights'].mean(), 2) # найти среднее число ночей провед. посетителями
#hotels['total_spend'] = hotels['adr'] * hotels['total_stay_nights']
#hotels = round(hotels['total_spend'].mean(), 2) # средняя общая сума бронирования за номер
#hotels = hotels[hotels['total_of_special_requests'] == 5][['name', 'email']] # найти имена и почту тех кто сделал по 5
# специальних запроса
#hotels = 100 * sum(hotels['is_repeated_guest'] == 1) / len(hotels) # процент повторного бронирования
#hotels = hotels['name'].apply(lambda name: name.split()[:-1]).value_caunts()[:5] # найти 5 фамилий встречающиея больше всех
#def grab_lastname(name):
#     return name.split()[:-1]
#hotels = hotels['name'].apply(grab_lastname).value_caunts()[:5]
#hotels['total_kids'] = hotels['babies'] + hotels['children']
#hotels = hotels.sort_values('total_kids', ascending=False)[['name', 'total_kids']] # имена людей с наибольшим числом детей
#hotels = hotels['phone_number'].apply(lambda num: num[:3]).value_caunts()[:3] # три кода телефона встречаются больше
#hotels = hotels['arrival_date_day_of_month'].apply(lambda day: day in range(1, 16)).sum() # сколько заселилось с 1 по 15
#def convert(day, month, year):
#    return f'{day}-{month}-{year}'
#hotels['data'] = np.vectorize(convert)(hotels['arrival_date_day_of_month'],
#                                       hotels['arrival_date_month'],
#                                       hotels['arrival_date_year'])
#hotels['data'] = pd.to_datetime(hotels['data'])
#hotels = hotels['data']
#hotels = hotels['data'].dt.day_name().value_caunts() # найти сколько людей в какой день недели заселились
print(hotels)