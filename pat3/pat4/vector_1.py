import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.preprocessing import StandardScaler
from sklearn.svm import SVR, LinearSVR
from sklearn.metrics import mean_absolute_error, mean_squared_error

df = pd.read_csv('cement_slump.csv')
sns.heatmap(df.corr(), annot=True)
df = df.columns
X = df.drop('Compressive Strength (28-day)(Mpa)', axis=1)
y = ['Compressive Strength (28-day)(Mpa)']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=101)# разбиваем данние
# на обучающий и тестовий набори для признаков и целевой переменой
scaler = StandardScaler() # обучаем обьект scaler на обучающих данних Х
scaled_X_train = scaler.fit_transform(X_train)
scaled_X_test = scaler.transform(X_test)

base_model = SVR()
base_model.fit(scaled_X_train, y_train)
SVR()
base_preds = base_model.predict(scaled_X_test)

ver = mean_squared_error(y_test, base_preds)
ver1 = np.sqrt(mean_squared_error(y_test, base_preds))
ver2 = y_test.mean()

pram_grid = {'C': [0.001, 0.01, 0.1, 0.5, 1], 'kernel': ['linear', 'rbf', 'poly'],
             'gamma': ['scale', 'auto'], 'degree': [2, 3, 4], 'epsilon': [0, 0.01, 0.1, 0.5, 1, 2]}
svr = SVR()
grid = GridSearchCV(svr, pram_grid)
grid.fit(scaled_X_train, y_train)
ver3 = grid.best_params_

grid_pred = grid.predict(scaled_X_test)
ver4 = mean_absolute_error(y_test, grid_pred)
ver5 = np.sqrt(mean_squared_error(y_test, grid_pred))

plt.show()
print(df)
