import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import classification_report
from sklearn.tree import plot_tree
from sklearn.ensemble import RandomForestClassifier, GradientBoostingClassifier, AdaBoostClassifier


df =pd.read_csv('Telco-Customer-Churn.csv')
#df = df.info()
#df = df.describe()
#df = df.isnull().sum()
#sns.countplot(data=df, x='Churn')
#sns.violinplot(data=df, x='Churn', y='TotalCharges')
#sns.boxplot(data=df, y='TotalCharges', x='Contract', hue='Churn')
# corr_df = pd.get_dummies(df[['gender', 'SeniorCitizen', 'Partner', 'Dependents', 'PhoneService', 'MultipleLines',
#                    'OnlineSecurity', 'OnlineBackup', 'DeviceProtection', 'TechSupport', 'InternetService',
#                    'StreamingTV', 'StreamingMovies', 'Contract', 'PaperlessBilling', 'PaymentMethod', 'Churn']]).corr()
# ver = corr_df['Churn_Yes'].sort_values().iloc[1: -1]
# sns.barplot(x=ver.index, y=ver.values)
# plt.xticks(rotation=90)
#df = df['Contract'].unique()
#df = df['tenure'].unique()
#sns.histplot(data=df, x='tenure', bins=60)
#sns.displot(data=df, x='tenure', bins=70, col='Contract', row='Churn')
#sns.scatterplot(data=df, x='MonthlyCharges', y='TotalCharges', hue='Churn')
# yes_churn = df.groupby(['Churn', 'tenure']).count().transpose()['Yes']
# no_churn = df.groupby(['Churn', 'tenure']).count().transpose()['No']
# churn_rate = 100 * yes_churn / (yes_churn + no_churn)
# df = churn_rate.transpose()['customerID']
# churn_rate.transpose()['customerID'].plot()
# def cohort(tenure):
#     if tenure < 13:
#         return '0-12 mons'
#     elif tenure <25:
#         return '13-24 mons'
#     elif tenure < 49:
#         return '25-48 mons'
#     else:
#         return 'mo 48 mons'
#
# df['Tenure Cohort'] = df['tenure'].apply(cohort)
# df = df[['Tenure Cohort', 'tenure']]
#sns.scatterplot(data=df, x='MonthlyCharges', y='TotalCharges', hue='Tenure Cohort')
#sns.countplot(data=df, x='Tenure Cohort', hue='Churn')
#sns.catplot(data=df, x='Tenure Cohort', hue='Churn', kind='count', col='Contract')
X = df.drop(['Churn', 'customerID'])
X = pd.get_dummies(X, drop_first=True)
y = df['Churn']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.1, random_state=101)# разбиваем данние
# на обучающий и тестовий набори для признаков и целевой переменой
dt = DecisionTreeClassifier(max_depth=6)
dt.fit(X_train, y_train)
DecisionTreeClassifier(max_depth=6)
preds = dt.predict(X_test)
print(classification_report(y_test, preds))
imp_fiat = pd.DataFrame(index=X.columns, data=df.feature_importances_, columns=['Важность'])
imp_fiat = imp_fiat.sort_values('Важность')
imp_fiat = imp_fiat[imp_fiat['Важность']>0]
sns.barplot(data=imp_fiat, x=imp_fiat.index, y='Важность')
plt.xticks(rotation=90)
plot_tree(df)
rf =RandomForestClassifier()
rf.fit(X_train, y_train)
RandomForestClassifier()
preds = rf.predict(X_test)
print(classification_report(y_test, preds))
ada_model = AdaBoostClassifier(n_estimators=100)
gb_model = GradientBoostingClassifier()
ada_model.fit(X_train, y_train)
AdaBoostClassifier()
gb_model.fit(X_train, y_train)
GradientBoostingClassifier()
ada_preds = ada_model.predict(X_test)
gb_preds = gb_model.predict(X_test)
print(classification_report(y_test, ada_preds))
print(classification_report(y_test, gb_preds))



plt.show()
print(df)
