import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.preprocessing import PolynomialFeatures
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, mean_squared_error
from joblib import dump, load


df = pd.read_csv('Advertising.csv')
X = df.drop('sales', axis=1)
y = df['sales']
polynomial_converter = PolynomialFeatures(degree=2, include_bias=False)
polynomial_converter.fit(X)
PolynomialFeatures(include_bias=False)
poly_features = polynomial_converter.transform(X)
#poly_features = poly_features.shape
# polynomial_converter.fit_transform(X)# единая команда для 2-х методов
X_train, X_test, y_train, y_test = train_test_split(poly_features, y, test_size=0.3, random_state=101)
model = LinearRegression()
model.fit(X_train, y_train)
LinearRegression()
test_prediction = model.predict(X_test)
mae = mean_absolute_error(y_test, test_prediction)
mse = mean_squared_error(y_test, test_prediction)
rmse = np.sqrt(mse)
train_rmse_errors = []
test_rmse_errors = []

for d in range(1, 10):
    poly_converter = PolynomialFeatures(degree=d, include_bias=False)
    poly_features = poly_converter.fit_transform(X)
    X_train, X_test, y_train, y_test = train_test_split(poly_features, y, test_size=0.3, random_state=101)
    model = LinearRegression()
    model.fit(X_train, y_train)
    train_pred = model.predict(X_train)
    test_pred = model.predict(X_test)
    train_rmse = np.sqrt(mean_squared_error(y_train, train_pred))
    test_rmse = np.sqrt(mean_squared_error(y_test, test_pred))
    train_rmse_errors.append(train_rmse)
    test_rmse_errors.append(test_rmse)

plt.plot(range(1, 6), train_rmse_errors[:5], label='TREIN RMSE')
plt.plot(range(1, 6), test_rmse_errors[:5], label='TEST RMSE')
plt.xlabel('Степень полинома')
plt.ylabel('RMSE')
plt.legend()

plt.plot(range(1, 10), train_rmse_errors, label='TREIN RMSE')
plt.plot(range(1, 10), test_rmse_errors, label='TEST RMSE')
plt.xlabel('Степень полинома')
plt.ylabel('RMSE')
plt.legend()

final_poly_converter = PolynomialFeatures(degree=3, include_bias=False)
final_model = LinearRegression()
full_converted_X = final_poly_converter.fit_transform(X)
final_model.fit(full_converted_X, y)
LinearRegression()

dump(final_model, 'final_poly_model.joblib')
dump(final_poly_converter, 'final_converter.joblib')
loaded_converter = load('final_converter.joblib')
loaded_model = load('final_poly_model.joblib')
campaign = [[149, 22, 12]]
transformed_data = loaded_converter.fit_transform(campaign)
res = loaded_model.predict(transformed_data)


plt.show()
print(transformed_data)
print(res)
# print(train_rmse_errors)
# print(test_rmse_errors)
# print(mae)
# print(rmse)
#print(df.head())
#print(model.coef_)
#print(poly_features[0])

