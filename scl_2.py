import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, mean_squared_error
import scipy as sp
from joblib import dump, load

df = pd.read_csv('Advertising.csv')
# fig, axes = plt.subplots(nrows=1, ncols=3, figsize=(16, 6))
# axes[0].plot(df['TV'], df['sales'], 'o')
# axes[0].set_ylabel("Sales")
# axes[0].set_title("TV Spend")
#
# axes[1].plot(df['radio'], df['sales'], 'o')
# axes[1].set_title("Radio Spend")
# axes[1].set_ylabel("Sales")
#
# axes[2].plot(df['newspaper'], df['sales'], 'o')
# axes[2].set_title("Newspaper Spend")
# axes[2].set_ylabel("Sales")
# #plt.tight_layout()
# sns.pairplot(df)
X = df.drop('sales', axis=1)
y = df['sales']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=101)
model = LinearRegression()
model.fit(X_train, y_train)
LinearRegression()
test_prediction = model.predict(X_test)
# res = df['sales'].mean()
# sns.histplot(data=df, x='sales', bins=20)
res = mean_absolute_error(y_test, test_prediction)#средняя абсолютная ошибка
res1 = mean_squared_error(y_test, test_prediction)
res2 = np.sqrt(mean_squared_error(y_test, test_prediction))#среднее квадротичное отклонение
test_residuals = y_test - test_prediction
# sns.scatterplot(x=y_test, y=test_residuals)
# plt.axhline(y=0, color='r', ls='--')
# sns.displot(test_residuals, bins=25, kde=True)
# fig, ax = plt.subplots(figsize=(6, 8), dpi=100) # создаем обьект figure и оси для рисования графика
# sp.stats.probplot(test_residuals, plot=ax)# probplot возвращает значения, которие можно использовать при необходимости

final_model = LinearRegression()
final_model.fit(X, y)
LinearRegression()
res3 = final_model.coef_
dump(final_model, 'final_sales_model.joblib')
loaded_model = load('final_sales_model.joblib')
res4 = loaded_model.coef_
campaign = [[149, 22, 12]]
res5 = loaded_model.predict(campaign)


# y_hat = final_model.predict(X)
# fig, axes = plt.subplots(nrows=1, ncols=3, figsize=(16, 6))
# axes[0].plot(df['TV'], df['sales'], 'o')
# axes[0].plot(df['TV'], y_hat, 'o', color='red')
# axes[0].set_ylabel("Sales")
# axes[0].set_title("TV Spend")
#
# axes[1].plot(df['radio'], df['sales'], 'o')
# axes[1].plot(df['radio'], y_hat, 'o', color='red')
# axes[1].set_title("Radio Spend")
# axes[1].set_ylabel("Sales")
#
# axes[2].plot(df['newspaper'], df['sales'], 'o')
# axes[2].plot(df['newspaper'], y_hat, 'o', color='red')
# axes[2].set_title("Newspaper Spend")
# axes[2].set_ylabel("Sales")
# plt.tight_layout()
#sns.pairplot(df)

plt.show()
#print(test_residuals)
#print(res3)
print(res4)
#print(X.shape)
print(res5)
#print(res)
# print(res1)
# print(res2)
#print(test_prediction)
#print(model.predict(X_test))
# print(X_test.head())
# print(y_test.head())
# print(y_train)
# print(X_train)
# print(len(df))
