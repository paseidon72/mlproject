import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.cluster import KMeans, DBSCAN
from sklearn.preprocessing import StandardScaler, MinMaxScaler


df = pd.read_csv('wholesome_customers_data.csv')
#sns.scatterplot(data=df, x='Milk', y='Grocery', hue='Channel')
#sns.histplot(data=df, x='Milk', hue='Channel', palette='Set1', multiple='stack')
#sns.clustermap(df.drop(['Region', 'Channel'], axis=1).corr(), annot=True, row_cluster=False)
#sns.pairplot(df, hue='Region', palette='Set1')
#sns.pairplot(df, hue='Channel', palette='Set1')
scaler = StandardScaler()
scaled_X = scaler.fit_transform(df)

outliers_percent = []
for eps in np.linspace(0.001, 3, 50):
    dbscan = DBSCAN(eps=eps, min_samples=2 * scaled_X.shape[1])
    dbscan.fit(scaled_X)
    percent_outliers = 100 * np.sum(dbscan.labels_ == -1) / len(dbscan.labels_)
    outliers_percent.append(percent_outliers)

#sns.lineplot(x=np.linspace(0.001, 3, 50), y=outliers_percent)

dbscan = DBSCAN(eps=2, min_samples=2 * scaled_X.shape[1])
dbscan.fit(scaled_X)
#sns.scatterplot(data=df, x='Grocery', y='Milk', hue=dbscan.labels_, palette='Set1')
#sns.scatterplot(data=df, x='Detergents_Paper', y='Milk', hue=dbscan.labels_, palette='Set1')

df['Labels'] = dbscan.labels_
cats = df.drop(['Channel', 'Region'], axis=1)
cat_means = cats.groupby('Labels').mean()
# plt.figure(figsize=(10, 6), dpi=100)
# sns.heatmap(cat_means, annot=True)

# plt.figure(figsize=(10, 6), dpi=100)
# sns.heatmap(cat_means.loc[[0, 1]], annot=True)

scaler = MinMaxScaler()
scaled_cat_data = scaler.fit_transform(cat_means)
df = pd.DataFrame(scaled_cat_data, cat_means.index, cat_means.columns)
plt.figure(figsize=(10, 6), dpi=100)
#sns.heatmap(pd.DataFrame(scaled_cat_data, cat_means.index, cat_means.columns))
sns.heatmap(pd.DataFrame(scaled_cat_data, cat_means.index, cat_means.columns).loc[[0, 1]], annot=True)


plt.show()
print(df)
