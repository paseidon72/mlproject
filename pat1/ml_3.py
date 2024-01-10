import numpy as np
import pandas as pd

"""Работа с дата фреймами"""
np.random.seed(101)
mydata = np.random.randint(0, 101, (4, 3))
# print(mydata)
# myindex = ['CA', 'NY', 'AZ', 'TX']
# mycolumns = ['Jan', 'Feb', 'Mar']
#df = pd.DataFrame(data=mydata, index=myindex, columns=mycolumns)
# ver1 = df.info()
df1 = pd.read_csv('tips.csv')
ver2 = df1.columns # название колонок
ver3 = df1.index # название строк
ver4 = df1.head() # первие строки
ver5 = df1.tail() # последние строки
#ver6 = df1.info() # информация про таблицу
ver7 = df1.describe() # метрики для числових колонок
df1.describe().transpose() # поменять местами колонки с столбцами
ver8 = df1[['total_bill', 'tip']]
df1['tip_procent'] = 100 * df1['tip'] / df1['total_bill'] # подсчет значений и добавление колонки
ver9 = df1[['total_bill', 'tip', 'tip_procent']]
# df1.drop('name', axis=0) # удаление строк
df1 = df1.drop('tip_procent', axis=1) # удалене колонок
df1 = df1.set_index('Payment ID') # обьявить колонку индексом всей таблици
df1 = df1.reset_index() # сбросить индекс
df1 = df1.set_index('Payment ID')
ver10 = df1.iloc[0] # получение строки по числовому индексу
ver11 = df1.loc['Sun2959'] # получение строки по именованому индексу
ver12 = df1.iloc[0:4]
ver13 = df1.loc[['Sun2959', 'Sun4608']]
df1 = df1.drop('Sun2959', axis=0) # удаление строк
one_row = df1.iloc[0] # создание новой строки
df1 = df1._append(one_row) # вставка новой строки
print(df1)