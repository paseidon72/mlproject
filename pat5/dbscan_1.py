import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.cluster import KMeans, DBSCAN


two_blobs = pd.read_csv('cluster_two_blobs.csv')
two_blobs_outliers = pd.read_csv('cluster_two_blobs_outliers.csv')
#sns.scatterplot(data=two_blobs, x='X1', y='X2')
#sns.scatterplot(data=two_blobs_outliers, x='X1', y='X2')


def display_categories(model, data):
    labels = model.fit_predict(data)
    #sns.scatterplot(data=data, x='X1', y='X2', hue=labels, palette='Set1')


#dbscan = DBSCAN()
#display_categories(dbscan, two_blobs)
#display_categodries(dbscan, two_blobs_outliers)
dbscan = DBSCAN(eps=0.7)
display_categories(dbscan, two_blobs_outliers)

np.sum(dbscan.labels_ == -1) #количество точек вибросов
100 * np.sum(dbscan.labels_ == -1) / len(dbscan.labels_) #процент точек класифицированих как виброси

# outliers_percent = []
# number_of_outliers = []
# for eps in np.linspace(0.001, 7, 200):
#     dbscan = DBSCAN(eps=eps)
#     dbscan.fit(two_blobs_outliers)
#     number_of_outliers.append(np.sum(dbscan.labels_ == -1))
#     percent_outliers = 100 * np.sum(dbscan.labels_ == -1) / len(dbscan.labels_)
#     outliers_percent.append(percent_outliers)

# sns.lineplot(x=np.linspace(0.001, 7, 200), y=number_of_outliers)
# plt.xlim(0, 2)
# plt.ylim(0, 10)
# plt.hlines(y=3, xmin=0, xmax=2, colors='red')

# sns.lineplot(x=np.linspace(0.001, 7, 200), y=outliers_percent)
# plt.xlim(0, 2)
# plt.ylim(0, 10)
# plt.hlines(y=1, xmin=0, xmax=2, colors='red')


outliers_percent = []
number_of_outliers = []
for n in np.arange(1, 100):
    dbscan = DBSCAN(min_samples=n)
    dbscan.fit(two_blobs_outliers)
    number_of_outliers.append(np.sum(dbscan.labels_ == -1))
    percent_outliers = 100 * np.sum(dbscan.labels_ == -1) / len(dbscan.labels_)
    outliers_percent.append(percent_outliers)

sns.lineplot(x=np.arange(1, 100), y=outliers_percent)



plt.show()
print(two_blobs)
print(two_blobs_outliers)
