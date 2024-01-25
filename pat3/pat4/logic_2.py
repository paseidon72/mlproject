import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegressionCV
from sklearn.metrics import confusion_matrix, classification_report, precision_recall_curve, roc_curve, pair_confusion_matrix

df = pd.read_csv('heart.csv')
'''проверка отсутствующих значений'''
df.info()
df.isnull().sum()
'''изучить характеристики числових колонок'''
df.describe().transponse()
'''визуализация целевой переменной'''
sns.countplot(x='target', data=df)
'''график связи между колонками'''
sns.pairplot(df[['age', 'trestbps', 'chol', 'thalach', 'target']], hue='target')
'''построить тепловую карту кореляции между колонками'''
plt.figure(figsize=(12, 8), dpi=100)
sns.heatmap(df.corr(), annot=True, cmap='viridis')

X = df.drop('target', axis=1) #очищаем данние для признаков по-Х
y = df['target'] #для целевой переменной по-у

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.1, random_state=101)# разбиваем данние
# на обучающий и тестовий набори для признаков и целевой переменой
scaler = StandardScaler() # обучаем обьект scaler на обучающих данних Х
scaled_X_train = scaler.fit_transform(X_train)
scaled_X_test = scaler.transform(X_test)
'''модель логической регресии'''
log_model = LogisticRegressionCV()
log_model.fit(scaled_X_train, y_train)
LogisticRegressionCV()
log_model.C_ # наилучшее значение
log_model.coef_ # коефициенти
'''график коефициентов логистической регресии'''
coefs = pd.Series(index=X.columns, data=log_model.coef_[0])
coefs = coefs.sort_values()
sns.barplot(x=coefs.index, y=coefs.values)
'''оценка работи модели'''
y_pred = log_model.predict(scaled_X_test)
confusion_matrix(y_test, y_pred)
pair_confusion_matrix(log_model, scaled_X_test, y_test)
print(classification_report(y_test, y_pred))
precision_recall_curve(log_model, scaled_X_test)
roc_curve(log_model, scaled_X_test, y_test)

patient = [[54., 1., 0., 122., 286., 0., 0., 116., 1., 3.2, 1., 2., 2.]]
log_model.predict(patient)
log_model.predict_proba(patient)


plt.show()
print(df)
