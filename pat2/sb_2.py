import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('dm_office_sales.csv')
#sns.rugplot(x='salary', data=df)
#sns.displot(data=df, x='salary')
#sns.kdeplot(data=df, x='salary')
np.random.seed(42)
sample_ages = np.random.randint(0, 100, 200)
sample_ages = pd.DataFrame(sample_ages, columns=['age'])
#sns.rugplot(data=sample_ages, x='age')
#sns.displot(data=sample_ages, x='age', rug=True, bins=30, kde=True)
sns.kdeplot(data=sample_ages, x='age', clip=[0, 100], bw_adjust=0.5, fill=True)
plt.show()