import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('StudentsPerformance.csv')
#plt.figure(figsize=(10, 4), dpi=100)
#sns.boxplot(data=df, y='math score', x='test preparation course')
#sns.boxplot(data=df, y='reading score', x='parental level of education', hue='test preparation course')
#sns.violinplot(data=df, y='reading score', x='parental level of education', hue='test preparation course')
#sns.swarmplot(data=df, x='math score', y='gender', size=2, hue='test preparation course', dodge=True)
#sns.boxenplot(data=df, x='math score', y='test preparation course', hue='gender')
#ns.jointplot(data=df, x='math score', y='reading score', kind='hex')
#sns.jointplot(data=df, x='math score', y='reading score', kind='kde', fill=True)
#sns.jointplot(data=df, x='math score', y='reading score', hue='gender')
#sns.pairplot(data=df, hue='gender', corner=True)
#sns.catplot(data=df, x='gender', y='math score', kind='box', col='lunch', row='test preparation course')
g = sns.PairGrid(data=df, hue='gender')
g = g.map_upper(sns.scatterplot)
g = g.map_diag(sns.kdeplot)
g = g.map_lower(sns.kdeplot)
g = g.add_legend()
plt.show()