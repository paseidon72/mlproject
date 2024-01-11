import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('country_table.csv')
df = df.set_index('Countries')
#sns.heatmap(data=df.drop('Life expectancy', axis=1), linewidths=0.5, annot=True)
#sns.clustermap(data=df.drop('Life expectancy', axis=1), linewidths=0.5, annot=True)
sns.clustermap(data=df.drop('Life expectancy', axis=1), linewidths=0.5, annot=True, col_cluster=False)
plt.show()