import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.preprocessing import PolynomialFeatures
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import Ridge
from sklearn.metrics import mean_absolute_error, mean_squared_error
from sklearn.linear_model import RidgeCV
from sklearn.linear_model import LassoCV
from sklearn.linear_model import ElasticNetCV



df = pd.read_csv('Advertising.csv')

X = df.drop('sales', axis=1)
y = df['sales']
polynomial_converter = PolynomialFeatures(degree=3, include_bias=False)
poly_features = polynomial_converter.fit_transform(X)
X_train, X_test, y_train, y_test = train_test_split(poly_features, y, test_size=0.3, random_state=101)
scaler = StandardScaler()
scaler.fit(X_train)
StandardScaler()
X_train = scaler.transform(X_train)
X_test = scaler.transform(X_test)

ridge_model = Ridge(alpha=10)
ridge_model.fit(X_train, y_train)
Ridge(alpha=10)

test_predictions = ridge_model.predict(X_test)
mae = mean_absolute_error(y_test, test_predictions)
mse = mean_squared_error(y_test, test_predictions)
rmse = np.sqrt(mse)

ridge_cv_model = RidgeCV(alphas=(0.1, 1.0, 10.0), scoring='neg_root_mean_squared_error')
ridge_cv_model.fit(X_train, y_train)
RidgeCV(alphas=(0.1, 1.0, 10.0))
res = ridge_cv_model.alpha_

test_predictions = ridge_cv_model.predict(X_test)
mae1 = mean_absolute_error(y_test, test_predictions)
mse = mean_squared_error(y_test, test_predictions)
rmse1 = np.sqrt(mse)
res1 = ridge_cv_model.coef_

lasso_cv_model = LassoCV(eps=0.001, n_alphas=100, cv=5, max_iter=1000000)
#lasso_cv_model = LassoCV(eps=0.1, n_alphas=100, cv=5)
lasso_cv_model.fit(X_train, y_train)
LassoCV(cv=5, max_iter=1000000)
#LassoCV(cv=5, eps=0.1)
res2 = lasso_cv_model.alpha_
test_predictions = lasso_cv_model.predict(X_test)
mae2 = mean_absolute_error(y_test, test_predictions)
mse = mean_squared_error(y_test, test_predictions)
rmse2 = np.sqrt(mse)
res3 = lasso_cv_model.coef_

elastic_model = ElasticNetCV(l1_ratio=[.1, .5, .7, .9, .95, .99, 1],
                             eps=0.001, n_alphas=100, max_iter=1000000)
elastic_model.fit(X_train, y_train)
ElasticNetCV(l1_ratio=[.1, .5, .7, .9, .95, .99, 1], max_iter=1000000)
mod = elastic_model.l1_ratio_
mod1 = elastic_model.alpha_
test_predictions = lasso_cv_model.predict(X_test)
mae3 = mean_absolute_error(y_test, test_predictions)




#plt.show()
print(mod)
print(mod1)
print(mae3)
# print(res3)
# print(rmse2)
# print(mae2)
# print(res2)
#print(res1)
# print(mae1)
# print(rmse1)
#print(res)
# print(mae)
# print(rmse)
#print(df.head())
#print(poly_features.shape)
#print(X_train.shape)
#print(X_train[0])
#print(X_test[0])
#print(poly_features[0])
