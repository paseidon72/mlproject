import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.preprocessing import StandardScaler
from sklearn.svm import SVC
from sklearn.metrics import confusion_matrix, classification_report

df = pd.read_csv('wine_fraud.csv')
df['quality'].unique()
sns.countplot(x='quality', data=df)
sns.countplot(x='quality', data=df, hue='type')

reds = df[df['type']=='red']
writes = df[df['type']=='write']

ver = len(reds[reds['quality']=='Fraud']) * 100/len(reds)
ver1 = len(writes[writes['quality']=='Fraud']) * 100/len(writes)

df['Fraud'] = df['quality'].map({'Legit': 0, 'Fraud': 1})
ver2 = df.corr()['Fraud'][:-1].sort_values().plot(kind='bar')

sns.clustermap(df.corr(), cmap='viridis')
df = df.drop('Fraud', axis=1)
df['type'] = pd.get_dummies(df['type'], drop_first=True)

X = df.drop('quality', axis=1)
y = df['quality']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.1, random_state=101)# разбиваем данние
# на обучающий и тестовий набори для признаков и целевой переменой
scaler = StandardScaler() # обучаем обьект scaler на обучающих данних Х
scaled_X_train = scaler.fit_transform(X_train)
scaled_X_test = scaler.transform(X_test)

svc = SVC(class_weight='balanced')
pram_grid = {'C': [0.001, 0.01, 0.1, 0.5, 1]}
grid = GridSearchCV(svc, pram_grid)
grid.fit(scaled_X_train, y_train)
ver3 = grid.best_params_

grid_preds = grid.predict(scaled_X_test)
confusion_matrix(y_test, grid_preds)
print(classification_report(y_test, grid_preds))


plt.show()
print(df)
