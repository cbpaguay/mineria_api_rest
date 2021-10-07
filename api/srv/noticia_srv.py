from joblib import load
from nltk.corpus import stopwords
from nltk.stem import SnowballStemmer
import re
import nltk
from sklearn.feature_extraction.text import CountVectorizer
from api.srv import db_postgres_srv as dbs
from api.srv import sector_srv as ss
import os
from langdetect import detect
from spanlp.palabrota import Palabrota
from spanlp.domain.countries import Country

palabrota = Palabrota()

nltk.download('stopwords')

directorio = os.path.dirname(__file__).replace("srv", "data")


def init():
    vectorizer = CountVectorizer()
    modelo = load(directorio + "/modelo.joblib")
    X = load(directorio + "/x_t.joblib")
    y = load(directorio + "/y_t.joblib")
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
    idioma = detect(item.get("noticia").lower())
    coordenadas = item.get("coordenadas")
    #idioma = "es"
    item['sector'] = ss.find_sector(coordenadas)
    if idioma in ['es', 'pt']:
        palabrota = Palabrota(censor_char="*", countries=[Country.ECUADOR], include=["vrg", "hpta",
                                                                                     "chch", "mmv",
                                                                                     "ctm", "mrd", "mierda"])
        modelo, vectorizer = init()
        noticia = stemming(item.get("noticia").lower())
        data = vectorizer.transform([noticia])
        resultado = modelo.predict(data)
        item['etiqueta'] = int(resultado[0])
        item['noticia'] = palabrota.censor(item.get("noticia"))
        
        dbs.insert_new(item)
    else:
        item['etiqueta'] = 2
    return item
