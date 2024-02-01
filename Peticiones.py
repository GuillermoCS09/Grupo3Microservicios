import requests

# Agregar un nuevo usuario
url_agregar_usuario = "http://127.0.0.1:5003/agregar_usuario"
data_usuario = {"nombre": "Nuevousuario"}
response_usuario = requests.post(url_agregar_usuario, json=data_usuario)
print("Respuesta del servicio de usuarios:", response_usuario.status_code)
print(response_usuario.json())

# Agregar un nuevo pedido
url_agregar_pedido = "http://127.0.0.1:5003/agregar_pedido"
data_pedido = {"producto": "NuevoProducto", "usuario_id": 1}
response_pedido = requests.post(url_agregar_pedido, json=data_pedido)
print("Respuesta del servicio de pedidos:", response_pedido.status_code)
print(response_pedido.json())



