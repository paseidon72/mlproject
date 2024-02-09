import numpy as np
import pandas as pd


df = pd.read_csv('moviereviews.csv')
#df = df.isnull().sum()
#df = df.dropna()
df = df['review'].str.isspace()
#df = df['review'].apply(lambda review:review=="")

print(df)
