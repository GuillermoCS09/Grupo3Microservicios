# orders_service.py
from flask import Flask, jsonify, request

app = Flask(__name__)

pedidos = [
    {"id": 1, "producto": "Laptop", "usuario_id": 1},
    {"id": 2, "producto": "Telefono", "usuario_id": 2},
]

@app.route('/pedidos', methods=['GET'])
def obtener_pedidos():
    return jsonify({"pedidos": pedidos})

@app.route('/pedidos', methods=['POST'])  # Cambiado para permitir solicitudes POST
def agregar_pedido():
    nuevo_pedido = request.json
    nuevo_pedido["id"] = len(pedidos) + 1
    pedidos.append(nuevo_pedido)
    return jsonify({"mensaje": "Pedido agregado con éxito", "pedido": nuevo_pedido}), 201

@app.route('/pedidos/<int:pedido_id>', methods=['GET'])
def obtener_pedido(pedido_id):
    pedido = next((order for order in pedidos if order["id"] == pedido_id), None)
    if pedido:
        return jsonify({"pedido": pedido})
    else:
        return jsonify({"mensaje": "Pedido no encontrado"}), 404

if __name__ == '__main__':
    app.run(debug=True, port=5002)
