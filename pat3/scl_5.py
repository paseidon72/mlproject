import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


def create_ages(mu=50, sigma=13, num_samples=100, seed=42):
    np.random.seed(seed)
    sample_ages = np.random.normal(loc=mu, scale=sigma, size=num_samples)
    sample_ages = np.round(sample_ages, decimals=0)
    return sample_ages
sample = create_ages()
#sns.displot(sample, bins=20)
#sns.boxplot(x=sample)
ser = pd.Series(sample)
#ser = ser.describe()
IQR = 55.25000 - 42.00000
lower_limit = 42.0 - 1.5 * IQR
ser = ser[ser > lower_limit]
q75, q25 = np.percentile(sample, [75, 25])
iqr = q75 - q25
lower = q25 - 1.5 * iqr
df = pd.read_csv('Ames_Housing_Data.csv')
#prise = df[(df['Overall Qual'] > 8) & (df['SalePrice'] < 200000)]
prise = df[(df['Gr Liv Area'] > 4000) & (df['SalePrice'] < 200000)]
drop_ind = df[(df['Gr Liv Area'] > 4000) & (df['SalePrice'] < 200000)].index
df = df.drop(drop_ind, axis=0)

#df.corr()['SalePrice'].sort_values()
#sns.scatterplot(x='Overall Qual', y='SalePrice', data=df)
sns.scatterplot(x='Gr Liv Area', y='SalePrice', data=df)




plt.show()
#print(drop_ind)
#print(prise)
#print(df)
#print(lower)
# print(q25)
# print(q75)
#print(ser)
#print(lower_limit)
#print(sample)
