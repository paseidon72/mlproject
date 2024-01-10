import numpy as np
import pandas as pd

"""Работа с фильтрами"""

df1 = pd.read_csv('tips.csv')
ver1 = df1['total_bill'] > 40
ver2 = df1[ver1]
ver3 = df1[df1['total_bill'] > 40] # фильтрация по значениям
ver4 = df1[df1['sex'] == 'Male']
ver5 = df1[(df1['total_bill'] > 30) & (df1['sex'] == 'Male')]
options = ['Sat', 'Sun']
#ver6 = df1[df1['day'].isin(options)] # фильтрация по спискам значений
ver6 = df1[df1['day'].isin(['Sat', 'Sun'])]
print(ver6)