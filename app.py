from flask import Flask, jsonify, request
from srv import noticia_srv as ns, database_srv as dbs

app = Flask(__name__)


@app.route("/api/saludo")
def saludo():
    return jsonify({"mensaje":ns.saludo()})


@app.route("/api/noticia", methods=["POST"])    
def clasificar():
    return jsonify(ns.clasificador(request.json))

@app.route("/api/noticias")
def lista_noticias():
    return jsonify(dbs.find_all_news())

@app.route("/api/noticia/<id>")
def find_noticia(id):
    return jsonify(dbs.find_new(id))
        
"""
Enable CORS. Disable it if you don't need CORS
"""
@app.after_request
def after_request(response):
    response.headers["Access-Control-Allow-Origin"] = "*" # <- You can change "*" for a domain for example "http://localhost"
    response.headers["Access-Control-Allow-Credentials"] = "true"
    response.headers["Access-Control-Allow-Methods"] = "POST, GET, OPTIONS, PUT, DELETE"
    response.headers["Access-Control-Allow-Headers"] = "Accept, Content-Type, Content-Length, Accept-Encoding, X-CSRF-Token, Authorization"
    return response

if __name__ == '__main__':
    app.run(debug=True, port=8017)
