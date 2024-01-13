import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import ElasticNet
from sklearn.model_selection import GridSearchCV
from sklearn.metrics import mean_absolute_error, mean_squared_error



df = pd.read_csv('AMES_Final_DF.csv')
#df = df.head()

X = df.drop('SalePrice', axis=1) #очищаем данние для признаков по-Х
y = df['SalePrice'] #для целевой переменной по-у

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.1, random_state=101)# разбиваем данние
# на обучающий и тестовий набори для признаков и целевой переменой

scaler = StandardScaler() # обучаем обьект scaler на обучающих данних Х
scaled_X_train = scaler.fit_transform(X_train)
scaled_X_test = scaler.transform(X_test)
#StandardScaler()

base_elastic_model = ElasticNet(max_iter=1000000)
param_grid = {'alpha': [0.1, 5, 10, 100], 'l1_ratio': [.1, .7, .99, 1]}

grid_model = GridSearchCV(estimator=base_elastic_model, param_grid=param_grid,
                          scoring='neg_mean_squared_error', cv=5, verbose=1)
res = grid_model.fit(scaled_X_train, y_train)

res1 = grid_model.best_params_ # лучшая комбинация параметров

y_pred = grid_model.predict(scaled_X_test)

mean_absolute_error(y_test, y_pred)
np.sqrt(mean_squared_error(y_test, y_pred))
np.mean(df['SalePrice'])

print(res1)
