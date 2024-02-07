import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.ensemble import GradientBoostingClassifier
from sklearn.metrics import classification_report, accuracy_score

df = pd.read_csv('mushrooms.csv')
X = df.drop('class', axis=1)
X = pd.get_dummies(X, drop_first=True)
y = df['class']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.1, random_state=101)# разбиваем данние
# на обучающий и тестовий набори для признаков и целевой переменой
param_grid = {'n_estimators': [50, 100], 'learning_rate': [0.1, 0.05, 0.2], 'max_depth': [3, 4, 5]}
gd_model = GradientBoostingClassifier()
grid = GridSearchCV(gd_model, param_grid)
grid.fit(X_train, y_train)
GridSearchCV(estimator=GradientBoostingClassifier(),
             param_grid={'learning_rate': [0.1, 0.05, 0.2], 'max_depth': [3, 4, 5], 'n_estimators': [50, 100]})
# predictions = grid.predict(X_test)
# ver = grid.best_estimator_
# ver1 = grid.best_params_
#print(classification_report(y_test, predictions))
#ver2 = grid.best_estimator_.feature_importances_
feat_import = grid.best_estimator_.feature_importances_
imp_fiat = pd.DataFrame(index=X.columns, data=feat_import, columns=['Важность'])
imp_fiat = imp_fiat[imp_fiat['Важность']>0.0005]
imp_fiat = imp_fiat.sort_values('Важность')
sns.barplot(data=imp_fiat, x=imp_fiat.index, y='Важность')
plt.xticks(rotation=90)


plt.show()
#print(predictions)
print(imp_fiat)
