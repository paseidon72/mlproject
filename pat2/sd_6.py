import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('application_record.csv')
# employed = df[df['DAYS_EMPLOYED'] < 0] #находим отрицательние значения
# employed['DAYS_EMPLOYED'] = employed['DAYS_EMPLOYED'] * -1 # делаем отрицат. числа положительними
# employed['DAYS_BIRTH'] = employed['DAYS_BIRTH'] * -1 # меняем (-) на (+)
# sns.scatterplot(data=employed, y='DAYS_EMPLOYED', x='DAYS_BIRTH')
# df['YEARS'] = -1 * df['DAYS_BIRTH']/365 # вичислить число лет по числу дней
# sns.histplot(data=df, x='YEARS')
# bottom_half_income = df.nsmallest(n=int(len(df)/2), columns='AMT_INCOME_TOTAL')# делим всех кто получает з\п попалам
# # для посторения категориального графика
# sns.boxplot(data=bottom_half_income, y='AMT_INCOME_TOTAL', x='NAME_FAMILY_STATUS', hue='FLAG_OWN_REALTY')
#df.drop('FLAG_MOBIL', axis=1).corr()
#sns.heatmap(data=df.drop('FLAG_MOBIL', axis=1).corr())
sns.heatmap(data=df.drop('FLAG_MOBIL', axis=1).corr())
plt.show()
