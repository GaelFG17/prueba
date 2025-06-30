from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/mensaje', methods=['GET'])
def obtener_mensaje():
    texto_largo = (
        "Este es un texto largo de ejemplo. Puede contener varios párrafos, descripciones detalladas o cualquier otra "
        "información extensa que se desee devolver desde una API."
    )
    return jsonify({"mensaje": texto_largo})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=10000)
