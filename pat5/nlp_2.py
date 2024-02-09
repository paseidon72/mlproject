import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.linear_model import LogisticRegression
from sklearn.svm import SVC, LinearSVC
from sklearn.metrics import classification_report
from sklearn.pipeline import Pipeline


df = pd.read_csv('airline_tweets.csv')
#sns.countplot(data=df, x='airline_sentiment')
# sns.countplot(data=df, x='negativereason')
# plt.xticks(rotation=90)
#sns.countplot(data=df, x='airline', hue='airline_sentiment')
data = df[['airline_sentiment', 'text']]
X = data['text']
y = data['airline_sentiment']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=101)# разбиваем данние
# на обучающий и тестовий набори для признаков и целевой переменой
tfidf = TfidfVectorizer(stop_words='english')
tfidf.fit(X_train)
TfidfVectorizer(stop_words='english')
X_train_tfidf = tfidf.transform(X_train)
X_test_tfidf = tfidf.transform(X_test)

nb = MultinomialNB()
nb.fit(X_train_tfidf, y_train)
MultinomialNB()

log_model = LogisticRegression(max_iter=1000)
log_model.fit(X_train_tfidf, y_train)

rdf_svc = SVC()
rdf_svc.fit(X_train_tfidf, y_train)
SVC()

liner_svc = LinearSVC()
liner_svc.fit(X_train_tfidf, y_train)
LinearSVC()

def report(model):
    preds = model.predict(X_train_tfidf)
    print(classification_report(y_test, preds))

report(rdf_svc)

pipe = Pipeline([('tfidf', TfidfVectorizer()),
                 ('svc', LinearSVC())])

plt.show()
print(data)
