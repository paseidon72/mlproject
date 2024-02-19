import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.preprocessing import MinMaxScaler
from sklearn.cluster import AgglomerativeClustering
from scipy.cluster.hierarchy import dendrogram
from scipy.cluster import hierarchy



df = pd.read_csv('cluster_mpg.csv')
#df = df.describe()
df_w_dummies = pd.get_dummies(df.drop('name', axis=1))
scaler = MinMaxScaler()
scaled_data = scaler.fit_transform(df_w_dummies)
scaled_df = pd.DataFrame(scaled_data, columns=df_w_dummies.columns)
#sns.heatmap(scaled_df)
#sns.clustermap(scaled_df)
#sns.clustermap(scaled_df, row_cluster=False)
#sns.clustermap(scaled_df, col_cluster=False)
# model = AgglomerativeClustering(n_clusters=3)
# cluster_labels = model.fit_predict(scaled_df)
#plt.figure(figsize=(12, 4), dpi=100)
#sns.scatterplot(data=df, x='mpg', y='weight', hue=cluster_labels)
#sns.scatterplot(data=df, x='mpg', y='horsepower', hue=cluster_labels)
#sns.scatterplot(data=df, x='mpg', y='horsepower', hue=cluster_labels, palette='viridis')
model = AgglomerativeClustering(n_clusters=None, distance_threshold=2)
cluster_labels = model.fit_predict(scaled_df)
linkage_matrix = hierarchy.linkage(model.children_)
plt.figure(figsize=(15, 5), dpi=100)
#dendro = dendrogram(linkage_matrix)
dendro = dendrogram(linkage_matrix, truncate_mode='lastp', p=11)
#dendro = dendrogram(linkage_matrix, truncate_mode='level', p=3)



plt.show()
#print(linkage_matrix)
