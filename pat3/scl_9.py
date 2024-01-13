import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import Ridge
from sklearn.metrics import mean_squared_error



df = pd.read_csv('Advertising.csv')
#df = df.head()

X = df.drop('sales', axis=1) #очищаем данние для признаков по-Х
y = df['sales'] #для целевой переменной по-у

X_train, X_other, y_train, y_other = train_test_split(X, y, test_size=0.3, random_state=101)# разбиваем данние
# на обучающий и тестовий набори для признаков и целевой переменой
X_eval, X_test, y_eval, y_test = train_test_split(X_other, y_other, test_size=0.5, random_state=101)

scaler = StandardScaler() # обучаем обьект scaler на обучающих данних Х
scaler.fit(X_train)
StandardScaler()

X_train = scaler.transform(X_train) # применяем маштабирование scale для тестових данних Х
X_eval = scaler.transform(X_eval)
X_test = scaler.transform(X_test)

model_one = Ridge(alpha=100) # создаем модель
model_one.fit(X_train, y_train) # обучаем модель только на обучающем наборе данних
Ridge(alpha=100)
y_eval_pred = model_one.predict(X_eval) # применяем модель для тестових данних
mse = mean_squared_error(y_eval, y_eval_pred) # оценка работи модели

model_two = Ridge(alpha=1) # настройка гипер параметров
model_two.fit(X_train, y_train)
Ridge(alpha=1)
new_pred_eval = model_two.predict(X_eval)
mse1 = mean_squared_error(y_eval, new_pred_eval)

y_final_test_pred = model_two.predict(X_test)
mse2 = mean_squared_error(y_test, y_final_test_pred)


print(mse)
print(mse1)
print(mse2)
#print(df)
# print(len(df))
# print(len(X_train))
# print(len(X_eval))
# print(len(X_test))

