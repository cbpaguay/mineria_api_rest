from flask import request
from joblib import load
import pandas as pd
from nltk.stem.porter import PorterStemmer
from nltk.corpus import stopwords
from nltk.stem import SnowballStemmer
import re
import nltk
from sklearn.feature_extraction.text import CountVectorizer
nltk.download('stopwords')
    
def init():
    vectorizer = CountVectorizer()
    modelo = load('./data/modelo.joblib')
    X = load('./data/x_t.joblib')
    y = load('./data/y_t.joblib')
    X = vectorizer.fit_transform(X)
    modelo = modelo.fit(X,y)
    return modelo, vectorizer

def stemming(content):
    stem = SnowballStemmer(language='spanish')
    stemmed_content = re.sub('[^a-zA-Z]', ' ',content) # this basically replaces everything other than lower a-z & upper A-Z with a ' ', for eg apple,bananna --> apple bananna
    stemmed_content = stemmed_content.lower() # to make all text lower case
    stemmed_content = stemmed_content.split() # this basically splits the line into words with delimiter as ' '
    stemmed_content = [stem.stem(word) for word in stemmed_content if not word in stopwords.words('spanish')] # basically remove all the stopwords and apply stemming to the final data
    stemmed_content = ' '.join(stemmed_content) # this basically joins back and returns the cleaned sentence
    return stemmed_content

def saludo():
    return "Hola desde flask"

def clasificador(item):
    modelo, vectorizer = init()
    noticia = stemming(item.get("noticia"))
    data = vectorizer.transform([noticia])
    resultado = modelo.predict(data)
    return "Falsa" if resultado[0] == 1 else "Verdadera" 
 