import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
from sklearn.cluster import KMeans

image_as_array = mpimg.imread('palm_trees.jpg')
image_as_array.shape
plt.imshow(image_as_array)
h, w, c = image_as_array.shape
image_as_array2d = image_as_array.reshape(h*w, c)
model = KMeans(n_clusters=6)
labels = model.fit_predict(image_as_array2d)
rgb_code = model.cluster_centers_.round(0).astype(int)
rgb_code[labels]
quantized_image = np.reshape(rgb_code[labels], h, w, c)



plt.show()
#print(image_as_array)
