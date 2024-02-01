# users_service.py
from flask import Flask, jsonify, request

app = Flask(__name__)

usuarios = [
    {"id": 1, "nombre": "Juan"},
    {"id": 2, "nombre": "Maria"},
]

@app.route('/usuarios', methods=['GET'])
def obtener_usuarios():
    return jsonify({"usuarios": usuarios})

@app.route('/usuarios', methods=['POST'])  # Cambiado para permitir solicitudes POST
def agregar_usuario():
    nuevo_usuario = request.json
    nuevo_usuario["id"] = len(usuarios) + 1
    usuarios.append(nuevo_usuario)
    return jsonify({"mensaje": "Usuario agregado con éxito", "usuario": nuevo_usuario}), 201

@app.route('/usuarios/<int:usuario_id>', methods=['GET'])
def obtener_usuario(usuario_id):
    usuario = next((user for user in usuarios if user["id"] == usuario_id), None)
    if usuario:
        return jsonify({"usuario": usuario})
    else:
        return jsonify({"mensaje": "Usuario no encontrado"}), 404

if __name__ == '__main__':
    app.run(debug=True, port=5001)
