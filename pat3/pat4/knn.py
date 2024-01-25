import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import confusion_matrix, classification_report, accuracy_score
from sklearn.pipeline import Pipeline

df = pd.read_csv('gene_expression.csv')
# sns.scatterplot(data=df, x='Gene One', y='Gene Two', hue='Cancer Present', alpha=0.6, style='Cancer Present')
# plt.xlim(2, 6)
# plt.ylim(4, 8)
# sns.pairplot(data=df, hue='Cancer Present')
X = df.drop('Cancer Present', axis=1) #очищаем данние для признаков по-Х
y = df['Cancer Present'] #для целевой переменной по-у
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)# разбиваем данние
# на обучающий и тестовий набори для признаков и целевой переменой
scaler = StandardScaler() # обучаем обьект scaler на обучающих данних Х
scaled_X_train = scaler.fit_transform(X_train)
scaled_X_test = scaler.transform(X_test)

knn_model = KNeighborsClassifier(n_neighbors=1)
knn_model.fit(scaled_X_train, y_train)
y_pred = knn_model.predict(scaled_X_test)

error1 = confusion_matrix(y_test, y_pred)
res = df['Cancer Present'].value_counts()

test_error_rates = []
for k in range(1, 30):
    knn_model = KNeighborsClassifier(n_neighbors=k)
    knn_model.fit(scaled_X_train, y_train)
    y_pred_test = knn_model.predict(scaled_X_test)
    test_error = 1 - accuracy_score(y_test, y_pred_test)
    test_error_rates.append(test_error)

# plt.plot(range(1, 30), test_error_rates)
# plt.ylabel('ERROR RATE')
# plt.xlabel('K ближайших соседей')
# plt.ylim(0, 0.11)

scaler = StandardScaler()
knn = KNeighborsClassifier()
knn.get_params().keys()

operation = [('scaler', scaler), ('knn', knn)]
pipe = Pipeline(operation)

k_values = list(range(1, 20))
param_grid = {'knn__n_neighbors': k_values}
full_cv_classifier = GridSearchCV(pipe, param_grid, cv=5, scoring='accuracy')
full_cv_classifier.fit(X_train, y_train)
vel1 = full_cv_classifier.best_estimator_.get_params()
vel = full_cv_classifier.predict(X_test)

new_patient = [[3.8, 6.4]]
vel2 = full_cv_classifier.predict(new_patient)
vel3 = full_cv_classifier.predict_proba(new_patient)


plt.show()
# print(df)
# print(error1)
# print(classification_report(y_test, y_pred))
# print(res)
# print(test_error_rates)
# print(full_cv_classifier)
# print(vel)
# print(vel1)
#print(classification_report(y_test, vel))
print(vel2)
print(vel3)

