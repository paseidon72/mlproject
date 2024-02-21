import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA
from sklearn.datasets import load_breast_cancer



df = pd.read_csv('cancer_tumor_data_features.csv')
scaler = StandardScaler()
scaled_X = scaler.fit_transform(df)

pca_model = PCA(n_components=2)
# pca_model.fit(scaled_X)
# pca_model.transform(scaled_X)

# scaler = StandardScaler()
# scaled_X = scaler.fit_transform(df)
covariance_matrix = np.cov(scaled_X, rowvar=False)
eigen_values, eigen_vectors = np.linalg.eig(covariance_matrix)
num_components = 2
sorted_key = np.argsort(eigen_values)[::-1][:num_components]
eigen_values, eigen_vectors = eigen_values[sorted_key], eigen_vectors[:, sorted_key]
principal_components = np.dot(scaled_X, eigen_vectors)
cancer_dictionary = load_breast_cancer()
type(cancer_dictionary)
cancer_dictionary.keys()

pc_results = pca_model.fit_transform(scaled_X)
#plt.scatter(pc_results[:, 0], pc_results[:, 1], c=cancer_dictionary['target'])

ver = pca_model.components_
ver1 = pca_model.components_.shape
df_components = pd.DataFrame(pca_model.components_, index=['PC1', 'PC2'], columns=df.columns)

# plt.figure(figsize=(20, 2), dpi=100)
# sns.heatmap(df_components, annot=True)
ver2 = pca_model.explained_variance_ratio_
ver3 = np.sum(pca_model.explained_variance_ratio_)

explained_pc = []
for n in range(1, 30):
    pca = PCA(n_components=n)
    pca.fit(scaled_X)
    explained_pc.append(np.sum(pca.explained_variance_ratio_))
plt.plot(range(1, 30), explained_pc)
plt.xlabel('количество главних компонент')
plt.ylabel('explained_pc')
plt.ylim(0, 1)

plt.show()

