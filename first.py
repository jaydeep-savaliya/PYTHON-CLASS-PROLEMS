from sklearn.feature_extraction.text import CountVectorizer
c = CountVectorizer()
a =["jaydip madhubhai savaliya"]

data  = c.fit_transform(a)
print(c.vocabulary_)
print(data.toarray())