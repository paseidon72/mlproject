from sklearn.feature_extraction.text import CountVectorizer, TfidfTransformer, TfidfVectorizer



text = ['This is a line',
        'This is another line',
        'Completely different line ']
cv = CountVectorizer()
sparse_matrix = cv.fit_transform(text)
ver = sparse_matrix.todense()
ver1 = cv.vocabulary_
tfidf = TfidfTransformer()
ver2 = tfidf.fit_transform(sparse_matrix)
ver3 = ver2.todense()

tv = TfidfVectorizer()
tv_results = tv.fit_transform(text)
ver4 = tv_results.todense()

# print(ver)
# print(ver1)
print(ver4)
