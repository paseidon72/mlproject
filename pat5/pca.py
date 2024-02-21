import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.preprocessing import StandardScaler
from sklearn.datasets import load_breast_cancer


df = pd.read_csv('cancer_tumor_data_features.csv')
scaler = StandardScaler()
scaled_X = scaler.fit_transform(df)
covariance_matrix = np.cov(scaled_X, rowvar=False)
eigen_values, eigen_vectors = np.linalg.eig(covariance_matrix)
num_components = 2
sorted_key = np.argsort(eigen_values)[::-1][:num_components]
eigen_values, eigen_vectors = eigen_values[sorted_key], eigen_vectors[:, sorted_key]
principal_components = np.dot(scaled_X, eigen_vectors)
#plt.scatter(principal_components[:, 0], principal_components[:, 1])
cancer_dictionary = load_breast_cancer()
type(cancer_dictionary)
cancer_dictionary.keys()
plt.scatter(principal_components[:, 0], principal_components[:, 1], c=cancer_dictionary['target'])


plt.show()
print(df)
