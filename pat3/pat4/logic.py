import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report
from sklearn.metrics import plot_confusion_matrix
from sklearn.metrics import precision_score, recall_score


df = pd.read_csv('hearing_test.csv')
X = df.drop('test_result', axis=1)
y = df['test_result']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.1, random_state=101)# разбиваем данние
# на обучающий и тестовий набори для признаков и целевой переменой
scaler = StandardScaler() # обучаем обьект scaler на обучающих данних Х
scaled_X_train = scaler.fit_transform(X_train)
scaled_X_test = scaler.transform(X_test)

log_model = LogisticRegression()
log_model.fit(scaled_X_train, y_train)
LogisticRegression()
#res = log_model.coef_

y_pred = log_model.predict(scaled_X_test)
y_pred_proba = log_model.predict_proba(scaled_X_test)
accuracy_score(y_test, y_pred)
confusion_matrix(y_test, y_pred)
plot_confusion_matrix(log_model, scaled_X_test, y_test, normalize='true')
print(classification_report(y_test, y_pred))
precision_score(y_test, y_pred)
recall_score(y_test, y_pred)





# df = df.describe()
# df = df['test_result'].value_counts()
#sns.countplot(data=df, x='test_result')
#plt.figure(dpi=100)
#sns.boxplot(x='test_result', y='age', data=df)
#sns.boxplot(x='test_result', y='physical_score', data=df)
#sns.scatterplot(x='age', y='physical_score', data=df, hue='test_result')
#sns.pairplot(df, hue='test_result')
#sns.heatmap(df.corr(), annot=True)
#sns.scatterplot(x='physical_score', y='test_result', data=df)
# fig = plt.figure()
# ax = fig.add_subplot(projection='3d')
# #ax.scatter(df['age'], df['physical_score'], df['test_result'])
# ax.scatter(df['age'], df['physical_score'], df['test_result'], c=df['test_result'])



#plt.show()
print(df)
print(y_pred)
#print(res)
