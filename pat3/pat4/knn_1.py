import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import KNeighborsClassifier
from sklearn.pipeline import Pipeline
from sklearn.metrics import confusion_matrix, classification_report


df = pd.read_csv('sonar.all-data.csv')
df['Target'] = df['Label'].map({'R': 0, 'M': 1})
X = df.drop(['Target', 'Label'], axis=1) #очищаем данние для признаков по-Х
y = df['Label'] #для целевой переменной по-у
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.1, random_state=42)# разбиваем данние
# на обучающий и тестовий набори для признаков и целевой переменой
scaler = StandardScaler()
knn = KNeighborsClassifier()
operation = [('scaler', scaler), ('knn', knn)]
pipe = Pipeline(operation)
k_values = list(range(1, 30))
param_grid = {'knn__n_neighbors': k_values}
full_cv_classifier = GridSearchCV(pipe, param_grid, cv=5, scoring='accuracy')
full_cv_classifier.fit(X_train, y_train)
vel1 = full_cv_classifier.best_estimator_.get_params()

vel2 = pd.DataFrame(full_cv_classifier.cv_results_)['mean_test_score'].plot()
y_pred = full_cv_classifier.predict(X_test)
vel3 = confusion_matrix(y_test, y_pred)


# plt.figure(figsize=(8, 6))
# sns.heatmap(df.corr(), cmap='coolwarm')
# vel = np.abs(df.corr()['Target']).sort_values().tail(6)

plt.show()
# print(df)
# print(full_cv_classifier)
# print(vel1)
# print(vel2)
# print(vel3)
print(classification_report(y_test, y_pred))
