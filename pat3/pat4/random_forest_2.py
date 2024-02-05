import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report


df = pd.read_csv('data_banknote_authentication.csv')
#sns.pairplot(df, hue='Class')
X = df.drop('Class', axis=1)
y = df['Class']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.15, random_state=101)# разбиваем данние
# на обучающий и тестовий набори для признаков и целевой переменой
n_estimators = [64, 100, 128, 200]
max_features = [2, 3, 4]
bootstrap = [True, False]
oob_score = [True, False]
param_grid = {'n_estimator': n_estimators, 'max_features': max_features,
              'bootstrap': bootstrap, 'oob_score': oob_score}
# rfc = RandomForestClassifier()
# grid = GridSearchCV(rfc, param_grid)
# grid.fit(X_train, y_train)
rfc = RandomForestClassifier(max_features=2, n_estimators=64, oob_score=True)
rfc.fit(X_train, y_train)
RandomForestClassifier(max_features=2, n_estimators=64, oob_score=True)
vel = rfc.oob_score_
prediction = rfc.predict(X_test)
#print(classification_report(y_test, prediction))
errors = []
misclassifications = []
for n in range(1, 200):
    rfc = RandomForestClassifier(n_estimators=n, max_features=2)
    rfc.fit(X_train, y_train)
    preds = rfc.predict(X_test)
    err = 1 - accuracy_score(y_test, preds)
    n_missed = np.sum(preds != y_test)
    errors.append(err)
    misclassifications.append(n_missed)

#plt.plot(range(1, 200), errors)
plt.plot(range(1, 200), misclassifications)




plt.show()
#print(df)
#print(vel)
