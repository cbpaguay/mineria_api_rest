from flask import Flask, jsonify, request
from srv import noticia_srv as ns

app = Flask(__name__)


@app.route("/api/saludo")
def saludo():
    return jsonify({
        "mensaje":ns.saludo()
        })


@app.route("/api/noticia", methods=["POST"])    
def clasificar():
    return jsonify({
        "Etiqueta":ns.clasificador(request.json)
        })

if __name__ == '__main__':
    app.run(debug=True, port=8017)
