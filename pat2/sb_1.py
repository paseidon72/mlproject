import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


plt.figure(figsize=(12, 4), dpi=200)
sns.scatterplot(x='salary', y='sales', data=df, hue='level of education')
plt.show()