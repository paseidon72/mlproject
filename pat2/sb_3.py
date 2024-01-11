import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('dm_office_sales.csv')
df['division'].value_counts()
plt.figure(figsize=(10, 4), dpi=100)
#sns.countplot(data=df, x='level of education', hue='division')
sns.barplot(data=df, x='level of education', y='salary', estimator=np.mean, errorbar='sd', hue='division')
plt.legend(loc=(0.8, 0.8))

plt.show()