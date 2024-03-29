import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import GridSearchCV
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report

df = pd.read_csv('iris.csv')
#df = df['species'].value_counts()
#sns.pairplot(df, hue='species')
X = df.drop('species', axis=1)
y = df['species']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25, random_state=101)# разбиваем данние
# на обучающий и тестовий набори для признаков и целевой переменой
scaler = StandardScaler() # обучаем обьект scaler на обучающих данних Х
scaled_X_train = scaler.fit_transform(X_train)
scaled_X_test = scaler.transform(X_test)

log_model = LogisticRegression(solver='saga', multi_class='ovr', max_iter=5000)
penalty = ['l1', 'l2', 'elasticnet']
l1_ratio = np.linspace(0, 1, 20)
C = np.logspace(0, 10, 20)
param_grid = {'penalty': penalty, 'l1_ratio': l1_ratio, 'C': C}
grid_model = GridSearchCV(log_model, param_grid=param_grid)
grid_model.fit(scaled_X_train, y_train)
grid_model.best_params_
y_pred = grid_model.predict(scaled_X_test)
accuracy_score(y_test, y_pred)
confusion_matrix(y_test, y_pred)
plot_confusion_matrix(grid_model, scaled_X_test, y_test)
print(classification_report(y_test, y_pred))



plt.show()
print(df)
