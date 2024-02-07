import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.ensemble import AdaBoostClassifier
from sklearn.metrics import classification_report, accuracy_score


df = pd.read_csv('mushrooms.csv')
#sns.countplot(data=df, x='class')
#df = df.describe()
#df = df.describe().transpose()
#df = df.describe().transpose().reset_index()
# feat_uni = df.describe().transpose().reset_index().sort_values('unique')
# plt.figure(figsize=(14, 6), dpi=100)
# sns.barplot(data=feat_uni, x='index', y='unique')
# plt.xticks(rotation=90)
X = df.drop('class', axis=1)
X = pd.get_dummies(X, drop_first=True)
y = df['class']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.15, random_state=101)# разбиваем данние
# на обучающий и тестовий набори для признаков и целевой переменой
model = AdaBoostClassifier(n_estimators=1)
# predictions = model.predict(X_test)
# print(classification_report(y_test, predictions))
# ver = model.feature_importances_
# model.feature_importances_.argmax()
#sns.countplot(data=df, x='odor', hue='class')

# error_rates = []
# for n in range(1, 96):
#     model = AdaBoostClassifier(n_estimators=n)
#     model.fit(X_train, y_train)
#     preds = model.predict(X_test)
#     err = 1 - accuracy_score(y_test, preds)
#     error_rates.append(err)
# plt.plot(range(1, 96), error_rates)

# feats = pd.DataFrame(index=X.columns, data=model.feature_importances_, columns=['Важность'])
# imp_feats = feats[feats['Важность']>0]
# sns.barplot(data=imp_feats, x=imp_feats.index, y='Важность')



plt.show()
#print(feat_uni)
#print(model)
