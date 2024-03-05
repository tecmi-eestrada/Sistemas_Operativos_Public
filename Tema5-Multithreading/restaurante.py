import multiprocessing
import time

cocineros = ["Cocinero_1", "Cocinero_2", "Cocinero_3"]
meseros = [
    {
        "id":"Mesero_1",
        "status": False
    },
    {
        "id":"Mesero_2",
        "status": False
    },
    {
        "id":"Mesero_3",
        "status": False
    }
    ]
chef = "Chef"
gerente = "Gerente"
cajero = "Cajero"
barista = "Barista"
limpieza = ["Limpieza_1", "Limpieza_2", "Limpieza_3"]

def tomar_pedido(num_platillos):
    for i in range(num_platillos):
        mesa = i + 3
        print("Solicitar a cocinero su coccion")
        cocinar_platillo(i)
        entregar_platillo(mesa)


def cocinar_platillo(num_orden):
    print(f"Cocinando platillo #{num_orden}")
    time.sleep(3)
    print(f"Platillo #{num_orden} listo")

def entregar_platillo(id_mesa):
    for mesero in meseros:
        for id, status in meseros.items():
            if status == True:
                print(f"El {id} esta libre, entregara la orden")

def coordinar_restaurante():
    pass

def cobrar():
    pass

def limpiar():
    pass

def coordinar_cocina():
    pass
