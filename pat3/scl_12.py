import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import Ridge
from sklearn.linear_model import ElasticNet
from sklearn.model_selection import GridSearchCV
from sklearn.model_selection import cross_validate
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

base_elastic_net_model = ElasticNet()
param_grid = {'alpha': [0.1, 5, 50, 100], 'l1_ratio': [.1, .5, .7, .95, .99, 1]}

grid_model = GridSearchCV(estimator=base_elastic_net_model, param_grid=param_grid,
                          scoring='neg_mean_squared_error', cv=5, verbose=0)
res = grid_model.fit(X_train, y_train)

res1 = grid_model.best_estimator_ # лучшая комбинация параметров

res2 = pd.DataFrame(grid_model.cv_results_) # все результати

y_pred = grid_model.predict(X_test)

mse = mean_squared_error(y_test, y_pred) # оценка работи модели


print(mse)
