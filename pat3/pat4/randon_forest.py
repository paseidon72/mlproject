import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import confusion_matrix, classification_report


df = pd.read_csv('penguins_size.csv')
df = df.dropna()
X = pd.get_dummies(df.drop('species', axis=1), drop_first=True)
y = df['species']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=101)# разбиваем данние
# на обучающий и тестовий набори для признаков и целевой переменой
rfc = RandomForestClassifier(n_estimators=10, max_features='sqrt', random_state=101)
rfc.fit(X_train, y_train)
RandomForestClassifier(n_estimators=10, random_state=101)
preds = rfc.predict(X_test)
print(classification_report(y_test, preds))



plt.show()
# print(df)
# print(preds)
