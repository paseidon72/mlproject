import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import Ridge
from sklearn.model_selection import cross_val_score
from sklearn.metrics import mean_squared_error



df = pd.read_csv('Advertising.csv')
#df = df.head()

X = df.drop('sales', axis=1) #очищаем данние для признаков по-Х
y = df['sales'] #для целевой переменной по-у

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=101)# разбиваем данние
# на обучающий и тестовий набори для признаков и целевой переменой

scaler = StandardScaler() # обучаем обьект scaler на обучающих данних Х
scaler.fit(X_train)
StandardScaler()

X_train = scaler.transform(X_train) # применяем маштабирование scale для тестових данних Х
X_test = scaler.transform(X_test)

# model = Ridge(alpha=100) # создаем модель
# scores = cross_val_score(model, X_train, y_train, scoring='neg_mean_squared_error', cv=5)
model = Ridge(alpha=1)
scores = cross_val_score(model, X_train, y_train, scoring='neg_mean_squared_error', cv=5)
#scores1 = abs(scores.mean())
model.fit(X_train, y_train)
Ridge(alpha=1)

y_final_test_pred = model.predict(X_test)
mse = mean_squared_error(y_test, y_final_test_pred) # оценка работи модели


print(mse)
# print(scores)
# print(scores1)
