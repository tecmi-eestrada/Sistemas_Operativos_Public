# Programa que simula el funcionamiento de un restaurante
import time

def recibirClientes():
    for mesa in mesas:
        if mesa[1] == "Libre":
            mesa[1] = "En espera"
            print(f'Los clientes se sentaron en la mesa {mesa[0]}')
            buscarMesero(mesa[0])
            break
    pass

def buscarMesero(numeroMesa):
    for mesero in meseros:
        if mesero[1] == "En espera":
            # Cambiar estado de mesero
            mesero[1] = "Ocupado"
            # Asignar mesa al mesero
            mesero[2] = {"mesa": numeroMesa}
            print(f'El mesero {mesero[0]} esta atendiendo la mesa {numeroMesa}')

            atenderMesa(numeroMesa, mesero[0])
            break

def atenderMesa(numeroMesa, nombreMesero):
    # Esperar 5 segundos
    time.sleep(5)
    # Cambiar estado de mesero
    for mesero in meseros:
        if mesero[0] == nombreMesero:
            mesero[1] = "En espera"
            break
    # Buscar orden mas alta
    ordenMasAlta = 0
    for orden in ordenes:
        if orden[0] > ordenMasAlta:
            ordenMasAlta = orden[0]
    # Agregar orden a lista de ordenes
    ordenes.append([ordenMasAlta + 1, "En espera", {"mesa": numeroMesa}])
    print(f'La mesa {numeroMesa} fue atendida por el mesero {nombreMesero}')
    # Cambiar estado de mesa
    for mesa in mesas:
        if mesa[0] == numeroMesa:
            mesa[1] = "Atendida"
            break
    # Enviar orden a cocina
    time.sleep(5)
    print(f'La orden {ordenMasAlta + 1} fue entregada a cocina')
    buscarCocinero(ordenMasAlta + 1, nombreMesero, numeroMesa)
    
def buscarCocinero(numeroMesa, nombreMesero, numeroOrden):
    for cocinero in cocineros:
        if cocinero[1] == "En espera":
            # Cambiar estado de cocinero
            cocinero[1] = "Ocupado"
            # Asignar orden al cocinero
            cocinero[2] = {"orden": numeroOrden}
            # Cambiar estado de orden
            for orden in ordenes:
                if orden[0] == numeroOrden:
                    orden[1] = "En proceso"
                    break
            print(f'El cocinero {cocinero[0]} esta haciendo la orden {numeroOrden}')
            time.sleep(5)
            print(f'La orden {numeroOrden} esta esperando para ser entregada')
            # Cambiar estado de cocinero
            cocinero[1] = "En espera"
            # Cambiar estado de orden
            for orden in ordenes:
                if orden[0] == numeroOrden:
                    orden[1] = "Lista"
                    break
                entregarOrden(numeroOrden, nombreMesero, numeroMesa)
            break

def entregarOrden(numeroOrden, nombreMesero, numeroMesa):
    time.sleep(5)
    print(f'La orden {numeroOrden} fue entregada por el mesero {nombreMesero} a la mesa {numeroMesa}')
    for mesa in mesas:
        if mesa[0] == numeroMesa:
            mesa[1] = "Comiendo"
            break
    for orden in ordenes:
        if orden[0] == numeroOrden:
            orden[1] = "Entregada"
            break
    time.sleep(1)
    print(f'Los clientes de la mesa {numeroMesa} estan comiendo')
    time.sleep(5)
    print(f'Los clientes de la mesa {numeroMesa} terminaron de comer')
    for mesa in mesas:
        if mesa[0] == numeroMesa:
            mesa[1] = "Esperando limpieza"
            break
    time.sleep(1)
    print(f'La mesa {numeroMesa} esta esperando ser limpiada')
    limpiarMesa(numeroMesa)
    pass

def limpiarMesa(numeroMesa):
    for limpiador in limpieza:
        if limpiador[1] == "En espera":
            # Cambiar estado de limpiador
            limpiador[1] = "Ocupado"
            print(f'El limpiador {limpiador[0]} esta limpiando la mesa {numeroMesa}')
            time.sleep(5)
            print(f'La mesa {numeroMesa} fue limpiada')
            # Cambiar estado de limpiador
            limpiador[1] = "En espera"
            # Cambiar estado de mesa
            for mesa in mesas:
                if mesa[0] == numeroMesa:
                    mesa[1] = "Libre"
                    break
            break
    pass


if __name__ == '__main__':
    mesas = (
        # El primer valor es el numero de la mesa
        # Las mesas pueden tener los siguientes estados: Libre, En espera, Atendida, Comiendo, Esperando limpieza
        # El tercer valor es un diccionario con informacion de la orden, la cual ayuda a conectar las mesas con las ordenes
        [1, "Comiendo", {"orden": 1}],
        [2, "Libre", {"orden": "No hay orden"}],
        [3, "Libre", {"orden": "No hay orden"}],
        [4, "Libre", {"orden": "No hay orden"}],
        [5, "Libre", {"orden": "No hay orden"}]
    )
    
    # El primer valor es el numero de la orden
    # Las ordenes pueden tener los siguientes estados: En espera, En proceso, Lista, Entregada
    # El tercer valor es un diccionario con informacion de la mesa, la cual ayuda a conectar las ordenes con las mesas
    ordenes = [
        [1, "Entregada", {"mesa": 1}],
        
    ]
    
    # El primer valor es el nombre del mesero
    # Los meseros pueden tener los siguientes estados: En espera, Ocupado
    # El tercer valor es un diccionario con informacion de la mesa, la cual ayuda a conectar los meseros con las mesas
    meseros = (
        ["Juan", "Ocupado", {"mesa": 1}],
        ["Maria", "En espera", {"mesa": "No hay mesa"}],
        ["Pedro", "En espera", {"mesa": "No hay mesa"}],
        ["Luis", "En espera", {"mesa": "No hay mesa"}],
        ["Ana", "En espera", {"mesa": "No hay mesa"}]
    )
    
    # El primer valor es el nombre del cocinero
    # Los cocineros pueden tener los siguientes estados: En espera, Ocupado
    # El tercer valor es un diccionario con informacion de la orden, la cual ayuda a conectar los cocineros con las ordenes
    cocineros = (
        ["Carlos", "Ocupado", {"orden": 1}],
        ["Jose", "En espera", {"orden": "No hay orden"}],
        ["Rosa", "En espera", {"orden": "No hay orden"}],
        ["Sofia", "En espera", {"orden": "No hay orden"}],
        ["Luz", "En espera", {"orden": "No hay orden"}]
    )
    
    # El primer valor es el nombre del limpiador
    # Los limpiadores pueden tener los siguientes estados: En espera, Ocupado
    limpieza = (
        ["Roberto", "Ocupado"],
        ["Luisa", "En espera"],
    )
    
    # Este es el inicio del programa
    # El programa se ejecuta en un ciclo llamanado la siguiente funcion
    recibirClientes()
    
    # El programa funciona como un solo proceso, haciendo el proceso de un restaurante de manera secuencial
    # Sin embargo, el programa debe ser modificado para que funcione como un proceso paralelo
    # Automatizando el proceso de un restaurante