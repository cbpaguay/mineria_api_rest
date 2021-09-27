from flask import Flask, jsonify, request
from api.srv import db_postgres_srv as dbs
from api.srv import noticia_srv as ns
from api.srv import mapeo_srv as ms
import os

app = Flask(__name__)
port = int(os.environ.get("PORT", 5000))


@app.route("/")
def saludo():
    return jsonify({"mensaje": ns.saludo()})


@app.route("/api/noticia", methods=["POST"])
def clasificar():
    return jsonify(ns.clasificador(request.json))


@app.route("/api/noticias")
def lista_noticias():
    items = dbs.find_all_news()
    if (len(items) > 0):
        items = ms.mapeo_all(items)
    return jsonify(items)


@app.route("/api/noticias/reales")
def lista_noticias_reales():
    items = dbs.find_news_reals()
    if (len(items) > 0):
        items = ms.mapeo_all(items)
    return jsonify(items)


@app.route("/api/noticias/fakes")
def lista_noticias_fakes():
    items = dbs.find_news_fakes()
    if (len(items) > 0):
        items = ms.mapeo_all(items)
    return jsonify(items)

@app.route("/api/noticia/<id>")
def find_noticia(id):
    item = dbs.find_new(id)
    if (item != None):
        item = ms.mapeo_one(item)
    return jsonify(item)


"""
Enable CORS. Disable it if you don't need CORS
"""


@app.after_request
def after_request(response):
    response.headers[
        "Access-Control-Allow-Origin"] = "*"  # <- You can change "*" for a domain for example "http://localhost"
    response.headers["Access-Control-Allow-Credentials"] = "true"
    response.headers["Access-Control-Allow-Methods"] = "POST, GET, OPTIONS, PUT, DELETE"
    response.headers[
        "Access-Control-Allow-Headers"] = "Accept, Content-Type, Content-Length, Accept-Encoding, X-CSRF-Token, Authorization"
    return response


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=port, debug=False)
