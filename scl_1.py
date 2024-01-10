import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('Advertising.csv')
df['total_spend'] = df['TV'] + df['radio'] + df['newspaper']
sns.regplot(data=df, x='total_spend', y='sales')
X = df['total_spend']
Y = df['sales']
# Y = mx + b
# Y = B1 * x + B0
#res = np.polyfit(X, Y, deg=1)
# potential_spend = np.linspace(0, 500, 100)
# predicted_sales = 0.04868788 * potential_spend + 4.24302822
# plt.plot(potential_spend, predicted_sales, color='red')
spend = 200
predicted_sales = 0.04868788 * spend + 4.24302822
res = np.polyfit(X, Y, 3)
# Y = B3 * x^3 + B2 * x^2 +B1 * x + B0
pot_spend = np.linspace(0, 500, 100)
pred_sales = 3.07615033e-07 * pot_spend**3 +\
             -1.89392449e-04 * pot_spend**2 +\
             8.20886302e-02 * pot_spend + \
             2.70495053e+00
plt.plot(pot_spend, pred_sales, color='red')
plt.show()
#print(df.head())
print(res)
