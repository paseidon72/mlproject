import numpy as np
import pandas as pd

"""Робота с недостающими и отсутствующими даними"""

df = pd.read_csv('movie_scores.csv')
#df = df.isnull()
#df = df.notnull()
#df = df['pre_movie_score'].notnull()
#df = df[df['pre_movie_score'].notnull()]
#df = df[(df['pre_movie_score'].isnull()) & (df['first_name'].notnull())]
#df = df.dropna()
#df = df.dropna(thresh=1)
#df = df.dropna(axis=0)
#df = df.dropna(subset=['last_name'])
#df = df['pre_movie_score'].fillna(0)
#df = df['pre_movie_score'].fillna(df['pre_movie_score'].mean())
#df = df.fillna(df.mean())
airline_tix = {'first': 100, 'business': np.nan, 'economy_plus': 50, 'economy': 30}
ser = pd.Series(airline_tix)
ser = ser.interpolate()
print(ser)