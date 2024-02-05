import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, mean_squared_error
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import PolynomialFeatures
from sklearn.neighbors import KNeighborsRegressor
from sklearn.tree import DecisionTreeRegressor
from sklearn.svm import SVR
from sklearn.ensemble import RandomForestRegressor, GradientBoostingRegressor, AdaBoostRegressor


df = pd.read_csv('rock_density_xray.csv')
df.columns = ['Signal', 'Density']
#sns.scatterplot(x='Signal', y='Density', data=df)
X = df['Signal'].values.reshape(-1, 1)
y = df['Density']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.1, random_state=101)# разбиваем данние
# на обучающий и тестовий набори для признаков и целевой переменой
lr_model = LinearRegression()
lr_model.fit(X_train, y_train)
LinearRegression()
lr_preds = lr_model.predict(X_test)
ver = mean_absolute_error(y_test, lr_preds)
ver1 = np.sqrt(mean_squared_error(y_test, lr_preds))

signal_range = np.arange(0, 100)
signal_preds = lr_model.predict(signal_range.reshape(-1, 1))
sns.scatterplot(x='Signal', y='Density', data=df)
plt.plot(signal_range, signal_preds)

def run_model(model, X_train, y_train, X_test, y_test):
    # обучение модели
    model.fit(X_train, y_train)
    # вичисление метрик
    preds = model.predict(X_test)
    rmse = np.sqrt(mean_squared_error(y_test, preds))
    mae = mean_absolute_error(y_test, preds)
    print(f'MAE: {mae}')
    print(f'RMSE: {rmse}')
    # построение графика с результатами
    signal_range = np.arange(0, 100)
    signal_preds = model.predict(signal_range.reshape(-1, 1))
    sns.scatterplot(x='Signal', y='Density', data=df, color='black')
    plt.plot(signal_range, signal_preds)

#model = LinearRegression()
#run_model(model, X_train, y_train, X_test, y_test)

#pipe = make_pipeline(PolynomialFeatures(degree=6), LinearRegression())
#run_model(pipe, X_train, y_train, X_test, y_test)

k_values = [1, 5, 10]
for n in k_values:
    model = KNeighborsRegressor(n_neighbors=n)
    run_model(model, X_train, y_train, X_test, y_test)

#model = DecisionTreeRegressor()
#run_model(model, X_train, y_train, X_test, y_test)

svr = SVR()
param_grid = {'C': [0.01, 0.1, 1, 5, 10, 100, 1000], 'gamma': ['auto', 'scale']}
grid = GridSearchCV(svr, param_grid)
#run_model(grid, X_train, y_train, X_test, y_test)

#rfr = RandomForestRegressor(n_estimators=10)
#run_model(rfr, X_train, y_train, X_test, y_test)

#models = GradientBoostingRegressor()
#run_model(models, X_train, y_train, X_test, y_test)

modelse = AdaBoostRegressor()
run_model(modelse, X_train, y_train, X_test, y_test)


plt.show()
#print(df)
#print(lr_preds)
