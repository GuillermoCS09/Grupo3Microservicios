# admin_service.py
from flask import Flask, jsonify, request
import requests

app = Flask(__name__)

usuarios_service_url = "http://127.0.0.1:5001/usuarios"  # Cambiado a la ruta correcta
pedidos_service_url = "http://127.0.0.1:5002/pedidos"   # Cambiado a la ruta correcta

usuarios = []
pedidos = []

@app.route('/agregar_usuario', methods=['POST'])
def agregar_usuario():
    nuevo_usuario = request.json
    nuevo_usuario["id"] = len(usuarios) + 1
    usuarios.append(nuevo_usuario)

    # Enviar solicitud al servicio de usuarios
    requests.post(usuarios_service_url, json=nuevo_usuario)

    return jsonify({"mensaje": "Usuario agregado con éxito", "usuario": nuevo_usuario}), 201

@app.route('/agregar_pedido', methods=['POST'])
def agregar_pedido():
    nuevo_pedido = request.json
    nuevo_pedido["id"] = len(pedidos) + 1
    pedidos.append(nuevo_pedido)

    # Enviar solicitud al servicio de pedidos
    requests.post(pedidos_service_url, json=nuevo_pedido)

    return jsonify({"mensaje": "Pedido agregado con éxito", "pedido": nuevo_pedido}), 201

if __name__ == '__main__':
    app.run(debug=True, port=5003)
