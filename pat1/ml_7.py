import numpy as np
import pandas as pd

"""Групировка даних"""

df = pd.read_csv('mpg.csv')
#df = df.drop('name', axis=1)
#df = df.groupby(['model_year', 'cylinders']).max()
#df = df.groupby('model_year').describe().transpose()
#df = df.groupby('model_year').describe()
#year_cyl = df.groupby(['model_year', 'cylinders']).max()
#df = year_cyl.swaplevel()
#df = year_cyl.sort_index(level='model_year', ascending=False)
#df = year_cyl.loc[[70, 82]]
#df = year_cyl.index
#df = year_cyl.index.levels
#df = year_cyl.loc[(70, 4)]
#df = year_cyl.xs(key=70, level='model_year')
#df = year_cyl.xs(key=4, level='cylinders')
#df = df[df['cylinders'].isin([6, 8])]
#df = df[df['cylinders'].isin([6, 8])].groupby(['model_year', 'cylinders']).min()
#df = df.agg(['std', 'mean'])['mpg']
df = df.agg({'mpg': ['max', 'mean'], 'weight': ['mean', 'std']})
print(df)