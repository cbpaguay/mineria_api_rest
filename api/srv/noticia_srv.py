from joblib import load
from nltk.corpus import stopwords
from nltk.stem import SnowballStemmer
import re
import nltk
from sklearn.feature_extraction.text import CountVectorizer
from api.srv import db_postgres_srv as dbs
import os

nltk.download('stopwords')

directorio = os.path.dirname(__file__).replace("srv", "data")


def init():
    vectorizer = CountVectorizer()
    modelo = load(directorio + "/model1.joblib")
    X = load(directorio + "/x_t1.joblib")
    y = load(directorio + "/y_t1.joblib")
    X = vectorizer.fit_transform(X)
    modelo = modelo.fit(X, y)
    return modelo, vectorizer


def stemming(content):
    stem = SnowballStemmer(language='spanish')
    stemmed_content = re.sub('[^a-zA-Z]', ' ',
                             content)  # this basically replaces everything other than lower a-z & upper A-Z with a ' ', for eg apple,bananna --> apple bananna
    stemmed_content = stemmed_content.lower()  # to make all text lower case
    stemmed_content = stemmed_content.split()  # this basically splits the line into words with delimiter as ' '
    stemmed_content = [stem.stem(word) for word in stemmed_content if not word in stopwords.words(
        'spanish')]  # basically remove all the stopwords and apply stemming to the final data
    stemmed_content = ' '.join(stemmed_content)  # this basically joins back and returns the cleaned sentence
    return stemmed_content


def saludo():
    return "Hola :)"


def clasificador(item):
    modelo, vectorizer = init()
    noticia = stemming(item.get("noticia"))
    data = vectorizer.transform([noticia])
    resultado = modelo.predict(data)
    item['etiqueta'] = int(resultado[0])
    dbs.insert_new(item)
    return item
