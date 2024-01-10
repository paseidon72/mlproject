import pandas as pd
import os

"""Чтение и запись csv"""

#fail = os.getcwd()
df = pd.read_csv('example.csv')
#df = pd.read_csv('example.csv', header=None)
df.to_csv('newfail.csv', index=False)
df = pd.read_csv('newfail.csv')
print(df)
