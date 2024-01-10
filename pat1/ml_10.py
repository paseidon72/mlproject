import numpy as np
import pandas as pd
from datetime import datetime

"""Работа со временем"""

#data = pd.Series(['Nov 3, 19190', '2000-01-01', None])
#data = pd.to_datetime(data)
# data = pd.read_csv('RetailSales_BeerWineLiquor.csv')
# data['DATE'] = pd.to_datetime(data['DATE'])
# data = data['DATE']
data = pd.read_csv('RetailSales_BeerWineLiquor.csv', parse_dates=[0])
#data = data['DATE']
data = data.set_index('DATE')
data = data.resample(rule='A').mean()
print(data)