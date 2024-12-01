# -*- coding: utf-8 -*-

from flask import Flask, request, jsonify

app = Flask(__name__)


@app.route('/mensaje', methods=['POST'])
def recibir_mensaje():
    data = request.json
    if 'mensaje' in data:
        mensaje = data['mensaje']
        respuesta = f"Mensaje recibido: {mensaje}"
        print(respuesta)
        return jsonify({'respuesta': respuesta})
    else:
        return jsonify({'error': 'No se proporcionó ningún mensaje'}), 400


if __name__ == '__main__':
    print("Servidor Flask corriendo en http://127.0.0.1:5000")
    app.run(debug=True, port=5000)
