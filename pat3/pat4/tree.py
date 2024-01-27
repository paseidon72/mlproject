import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.tree import DecisionTreeClassifier, plot_tree
from sklearn.metrics import confusion_matrix, classification_report

df = pd.read_csv('penguins_size.csv')
df = df.dropna()
ver = df.isnull().sum()
ver1 = df['species'].unique()
ver2 = df['island'].unique()
ver3 = df['sex'].unique()
ver4 = df[df['sex'] == '.']
ver5 = df[df['species'] == 'Gentoo'].groupby('sex').describe().transpose()
df.at[336, 'sex'] = 'FEMALE'
ver6 = df.loc[336]
#sns.pairplot(df, hue='species')
#sns.catplot(x='species', y='culmen_length_mm', data=df, kind='box', col='sex')
X = pd.get_dummies(df.drop('species', axis=1), drop_first=True)
y = df['species']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=101)# разбиваем данние
# на обучающий и тестовий набори для признаков и целевой переменой
model = DecisionTreeClassifier()
model.fit(X_train, y_train)
DecisionTreeClassifier()
base_preds = model.predict(X_test)
#print(classification_report(y_test, base_preds))
ver7 = model.feature_importances_
ver8 = pd.DataFrame(index=X.columns, data=model.feature_importances_,
                    columns=['Важность признаков']).sort_values('Важность признаков')
# plt.figure(figsize=(12, 8), dpi=100)
# plot_tree(model, feature_names=X.columns, filled=True)

def report_model(model):
    model_preds = model.predict(X_test)
    print(classification_report(y_test, model_preds))
    plt.figure(figsize=(12, 8), dpi=100)
    plot_tree(model, feature_names=X.columns, filled=True)

#report_model(model)

pruned_tree = DecisionTreeClassifier(max_depth=2)
pruned_tree.fit(X_train, y_train)
DecisionTreeClassifier(max_depth=2)
#report_model(pruned_tree)

max_leaf_tree = DecisionTreeClassifier(max_leaf_nodes=3)
max_leaf_tree.fit(X_train, y_train)
DecisionTreeClassifier(max_leaf_nodes=3)
#report_model(max_leaf_tree)

entropy_tree = DecisionTreeClassifier(criterion='entropy')
entropy_tree.fit(X_train, y_train)
DecisionTreeClassifier(criterion='entropy')
report_model(entropy_tree)


plt.show()
#print(ver7)
#print(base_preds)
# print(df)
# print(ver)
# print(ver1)
# print(ver2)
# print(ver3)
# print(ver4)
# print(ver5)
# print(ver6)
#print(X)
#print(ver8)
