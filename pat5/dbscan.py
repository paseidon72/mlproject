import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.cluster import KMeans, DBSCAN


blobs = pd.read_csv('cluster_blobs.csv')
#sns.scatterplot(data=blobs, x='X1', y='X2')
moons = pd.read_csv('cluster_moons.csv')
#sns.scatterplot(data=moons, x='X1', y='X2')
circles = pd.read_csv('cluster_circles.csv')
#sns.scatterplot(data=circles, x='X1', y='X2')


def display_categories(model, data):
    labels = model.fit_predict(data)
    sns.scatterplot(data=data, x='X1', y='X2', hue=labels, palette='Set1')

# model = KMeans(n_clusters=3)
# display_categories(model, blobs)

# model = KMeans(n_clusters=2)
# display_categories(model, moons)

# model = KMeans(n_clusters=2)
# display_categories(model, circles)

# model = DBSCAN()
# display_categories(model, blobs)

# model = DBSCAN(eps=0.15)
# display_categories(model, moons)

model = DBSCAN(eps=0.15)
display_categories(model, circles)



plt.show()
# print(blobs)
# print(moons)
# print(circles)
