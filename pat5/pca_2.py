import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA
from mpl_toolkits import mplot3d


digits = pd.read_csv('digits.csv')
pixels = digits.drop('number_label', axis=1)

single_image = pixels.iloc[0]
single_image.to_numpy()
single_image.to_numpy().shape
number = single_image.to_numpy().reshape(8, 8)

#plt.imshow(number, cmap='gray')

scaler = StandardScaler()
scaled_pixels = scaler.fit_transform(pixels)

# pca_model = PCA(n_components=2)
# pca_pixels = pca_model.fit_transform(scaled_pixels)
# pca_model.explained_variance_ratio_
# np.sum(pca_model.explained_variance_ratio_)

#sns.scatterplot(pca_pixels[:,0], pca_pixels[:,1], hue=digits['number_label'].values, palette='Set1')

pca_model = PCA(n_components=3)
pca_pixels = pca_model.fit_transform(scaled_pixels)

#%matplotlib notebook
plt.figure(figsize=(8, 8), dpi=100)
ax = plt.axes(projection='3d')
ax.scatter3D(pca_pixels[:, 0], pca_pixels[:, 1], pca_pixels[:, 2], c=digits['number_label'])

plt.show()
print(pixels)
