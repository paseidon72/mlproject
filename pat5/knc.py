import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_score


df = pd.read_csv('bank-full.csv')
#df = df.info()
#df = df.describe()
#sns.histplot(data=df[df['pdays'] != 999], x='pdays')
# sns.histplot(data=df, x='duration', hue='contact')
# plt.xlim(0, 1000)
#sns.countplot(data=df, x='contact')
#sns.countplot(data=df, x='job', order=df['job'].value_counts().index)
#sns.countplot(data=df, x='education', order=df['education'].value_counts().index)
#sns.countplot(data=df, x='education', order=df['education'].value_counts().index, hue='default')
# sns.countplot(data=df, x='default')
# plt.xticks(rotation=90)
#sns.pairplot(df)
X = pd.get_dummies(df)
scaler = StandardScaler()
scaled_X = scaler.fit_transform(X)
#model = KMeans(n_clusters=2)
#cluster_labels = model.fit_predict(scaled_X)
#X['Cluster'] = cluster_labels
#ver = X.corr()['Cluster'].iloc[:-1].sort_values()
#X.corr()['Cluster'].iloc[:-1].sort_values().plot(kind='bar')

ssd = []
for k in range(2, 10):
    model = KMeans(n_clusters=k)
    model.fit(scaled_X)
    ssd.append(model.inertia_) # сума квадратов растояний от точек до центров кластеров

plt.plot(range(2, 10), ssd, 'o--')
pd.Series(ssd)
pd.Series(ssd).diff()
pd.DataFrame(data=zip(range(2, 10), pd.Series(ssd).diff()), columns=['K', 'SSD diff'])

silhouettes = []
for k in range(2, 10):
    model = KMeans(n_clusters=k)
    model.fit(scaled_X)
    silhouettes.append(silhouette_score(scaled_X, model.labels_)) # сума квадратов растояний от точек до центров кластеров


plt.show()
#print(X)
# print(X)
# print(ver)
#print(ssd)
