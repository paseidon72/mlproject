import numpy as np
import pandas as pd

"""Работа с методами функции Apply"""

df1 = pd.read_csv('tips.csv')

"""Применение функции для 1 колонки"""
def last_four(num):
    return str(num)[-4:]
#ver1 = df1['CC Number'].apply(last_four)
df1['last_four'] = df1['CC Number'].apply(last_four)

df1['total_bill'].mean() # среднее значение колонки
def yelp(price):
    if price < 10:
        return '$'
    elif price >= 10 and price < 30:
        return '$$'
    else:
        return '$$$'
df1['yelp'] = df1['total_bill'].apply(yelp)

"""Применени функции для нескольких колонок"""

def qualiti(total_bill, tip):
    if tip/total_bill > 0.25:
        return 'Щедрие чаевие'
    else:
        return 'Обичние чаєвие'

#ver1 = df1[['total_bill', 'tip']].apply(lambda df1: qualiti(df1['total_bill'], df1['tip']), axis=1)
df1['qualiti'] = df1[['total_bill', 'tip']].apply(lambda df1: qualiti(df1['total_bill'], df1['tip']), axis=1)
df1['qualiti'] = np.vectorize(qualiti)(df1['total_bill'], df1['tip'])

df1 = pd.read_csv('tips.csv')
df1.describe() # виводит основние характеристики для числових колонок
df1.describe().transpose() # поменять местами колонки строки (транспорнировать)
df1.sort_values('tip') # сортировка по колонке
df1.sort_values('tip', ascending=False) # сортировка в обратном порядке
df1.sort_values(['tip', 'size'], ascending=True) # сортировка по списку колонок
df1['tip'].max() # максимальное значение колонки
df1['tip'].idxmax() # индекс максимального значения колонки
df1.iloc[170] # поиск строки по индеку
df1['tip'].min() # минимальное значение колонки
df1['tip'].idxmin() # индекс минимального значения колонки
# df1.iloc[df1['tip'].min()]..df1.iloc[df1['tip'].max()]..df1.iloc[df1['tip'].idxmin()]..df1.iloc[df1['tip'].idxmax()]
df1.corr() # возвращает кореляцию между числовими колонками
df1['sex'].value_counts() # считает количество строк по заданому значению
df1['day'].unique() # получить уникальние значения в колонке
df1['day'].nunique() # получить количество уникальних значений в колонке
df1['sex'].replace('Femal', 'F') # замена значения в столбце
df1['sex'].replace(['Femal', 'Male'], ['F', 'M']) # тоже используя списки
mymap = {'Femal': 'F', 'Male': 'M'}
df1['sex'].map(mymap) # тоже используя словари
df1.duplicated() # проверка дубликатов строк
df1.drop_duplicates() # удаляет дубликати строк
df1['total_bill'].between(10, 20, inclusive=True) # найти значения в диапазоне 10-20 верхняя граница включена
df1[df1['total_bill'].between(10, 20, inclusive=True)] # виборка строк по предидущему условию
df1.nlargest(10, 'tip') # получить 10 строк с наибольшими значениями столбца
df1.nsmallest(10, 'tip') # получить 10 строк с наименьшими значениями столбца
df1.sample(5) # получить случайние строки
df1.sample(frac=0.1) # получить случайние строки в процентном виде тут 10% строк

