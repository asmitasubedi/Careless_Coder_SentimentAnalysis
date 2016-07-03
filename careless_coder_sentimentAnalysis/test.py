import pandas as pd
from flask import Flask
import os
import re
import numpy as np
import nltk
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfTransformer
from nltk.stem.porter import PorterStemmer
from sklearn.pipeline import Pipeline
from sklearn.linear_model import SGDClassifier
from sklearn.linear_model import LogisticRegression
nltk.download('stopwords')
from nltk.corpus import stopwords
from flask import render_template

df = pd.DataFrame()
tf = pd.DataFrame()
ndf=pd.DataFrame()
df = pd.read_csv('./news_data.csv')
tf = pd.read_csv('./testData.csv')
df.head(3)


def preprocessor(text):
       text = re.sub('[\W]+', ' ', text)
       return text

df['news']=df['news'].apply(preprocessor)
print(df['news'])

stop = stopwords.words('english')
def remove_stop_words(text):
       return [w for w in text.split() if w not in stop]
porter = PorterStemmer()
df['news']=df['news'].apply(remove_stop_words)
print(df['news'])

val=0
for x in df['news']:
               df['news'][val] = [porter.stem(word) for word in x]
               text=""
               for word in df['news'][val]:
                       text=text + word + " "
               df['news'][val]=text
               val+=1
print(df['news'])

count = CountVectorizer()
bag = count.fit_transform(df['news'])
print(count.vocabulary_)

print(bag.toarray())

tfidf = TfidfTransformer()
np.set_printoptions(precision=2)
print(tfidf.fit_transform(count.fit_transform(df['news'])).toarray())

text_clf = Pipeline([('vect', CountVectorizer()),('tfidf', TfidfTransformer()),('clf', LogisticRegression()),])

_ = text_clf.fit(df['news'],df['sentiment'])


predicted = text_clf.predict(tf['news'])
print(predicted)

good=[]
bad=[]
ind=0

home=np.mean(predicted == tf['sentiment'])
print("Accuracy: "+ str(home))
for p in predicted:
	if p==0:
		bad.append(tf['news'][ind])
		ind+=1
	else:
		good.append(tf['news'][ind])
		ind+=1
	

print("Good News")
print(good)

print("Bad News")
print(bad)


def myfunction():
	return bad, good







