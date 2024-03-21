import time
import json

# Ingresa cliente,se le dan alrededor de 5 seg en ser atendido
# para ser llevado a una mesa LIBRE y se le dan 10 seg en asignarle un mesero LIBRE, despues se le hace un pedido en 15 seg.
# REQUERIRA: numero de mesa, nombre del mesero, numero de orden.
        
# Para GESTIONAR MESA.
#REQUERIRA: numero de mesa y estado
def gestionar_mesa(mesas):
    mesas_dis = []
    for mesa in mesas:
        inf_mesa = {
            "Mesa": mesa,
            "Estado": "Libre" 
        }
        mesas_dis.append(inf_mesa)
    return mesas_dis

# Para ASIGNAR MESA se CAMBIA  el estado.
#REQUERIRA: numero de mesa y estado
def asignar_mesa(mesas):
    for mesa in mesas:
        if mesa["Estado"] == "Libre":
            mesa_asignada = {
                "Mesa": mesa["Mesa"],
                "Estado": "Ocupado"
            }
            mesa.update(mesa_asignada)
            return mesa
    return None

# Para GESTIONAR MESERO.
#REQUERIRA: nombre del mesero, estado, numero de mesa y orden
def gestionar_mesero(meseros):
    meseros_turno = []
    for mesero in meseros:
        inf_mesero = {
            "Mesero": mesero,
            "Estado": "Libre",
            "Mesa": 0,
            "Orden": 0
        }
        meseros_turno.append(inf_mesero)
    return meseros_turno

# Para ASIGNAR MESERO se debe CAMBIAR informacion del mesero.
#REQUERIRA: nombre del mesero, estado, numero de mesa y orden
def asignar_mesero(meseros, mesa, orden):
    for mesero in meseros:
        if mesero["Estado"] == "Libre":
            mesero_asignada = {
                "Mesero": mesero["Mesero"],
                "Mesa": mesa["Mesa"],
                "Orden": orden,
                "Estado": "Ocupado"
            }
            mesero.update(mesero_asignada)
            return mesero
    return None

# Para GESTIONAR ORDEN se debe COMPROBAR el estado "LIBRE".
#REQUERIRA: estado, orden, numero de mesa  y nombre del mesero
def gestionar_orden(ordenes):
    ordenes_dis = []
    for orden in ordenes:
        inf_orden = {
            "Orden": orden,
            "Estado": "Libre",
            "Mesero": "",
            "Mesa": 0  
        }
        ordenes_dis.append(inf_orden)
    return ordenes_dis

# Para ASIGNAR ORDEN se debe CAMBIAR informacion del mesero.
#REQUERIRA: estado, orden, numero de mesa  y nombre del mesero
def asignar_orden(ordenes, mesa, mesero):
    for orden in ordenes:
        if orden["Estado"] == "Libre":
            orden_asignada = {
                "Orden": orden["Orden"],
                "Estado": "Ocupado",
                "Mesero": mesero["Mesero"],
                "Mesa": mesa["Mesa"]       
            }
            orden.update(orden_asignada)
            return orden
    return None

# Se resguarda información de la mesa, mesero, orden, cocinero, limpieza. 
# REQUERIRA: mesa, mesero, orden, cocinero y limpieza
def guardar_informacion(mesas, meseros, ordenes, cocineros, limpieza):
    try:
        with open("mesas.json", "w") as f:
            json.dump(mesas, f)
        with open("meseros.json", "w") as f:
            json.dump(meseros, f)
        with open("ordenes.json", "w") as f:
            json.dump(ordenes, f)
        with open("cocineros.json", "w") as f:
            json.dump(cocineros, f)
        with open("limpieza.json", "w") as f:
            json.dump(limpieza, f)
    except Exception as e:
        print("No fue posible guardar la informacion")

def atender_cliente(mesa,mesero,orden):
    print("Atendido a cliente, esperando para asignar mesa...")
    time.sleep(5)
    mesa_asignada = asignar_mesa(mesa)
    #La mesa queda OCUPADA 
    if mesa_asignada:    
        print(f"           Su mesa sera la {mesa_asignada['Mesa']}")
        time.sleep(5)
        mesero_asignado = asignar_mesero(mesero, mesa_asignada, 0)
        #El mesero queda OCUPADO
        if mesero_asignado:
            print(f"        Su mesero sera {mesero_asignado['Mesero']}")
            time.sleep(5)
            orden_asignada = asignar_orden(orden, mesa_asignada, mesero_asignado)
            #La orden queda OCUPADA
            if orden_asignada:
                asignar_mesero(mesero, mesa_asignada, orden_asignada["Orden"])
                print(f"    Tomando orden {orden_asignada['Orden']} por {mesero_asignado['Mesero']}")
                time.sleep(5)
                return mesa_asignada, mesero_asignado, orden_asignada
            else:
                print("No es posible generar una orden, disculpe las molestias")
        else:
            print("No hay meseros disponibles, disculpe las molestias")
    else:
        print("No hay mesas disponibles, disculpe las molestias")
    return None

# Tras hacer pedido, a la mesa se le asigna un cocinero LIBRE (toma 10 seg en asignar), se le pone en espera unos 20 seg para generar el platillo y
# el MESERO esta en ESPERA, mientras el COCINERO esta OCUPADO, finaliza la generación de platillo y se pone en estado LIBRE al cocinero

# Para GESTIONAR COCINERO se debe COMPROBAR el estado "LIBRE".
#REQUERIRA: nombre del cocinero, estado y orden
def gestionar_cocinero(cocineros):
    inf_cocineros = []
    for cocinero in cocineros:
        cocinero = {
            "Cocinero": cocinero,
            "Estado": "Libre",
            "Orden": 0,   
        }
        inf_cocineros.append(cocinero)
    return inf_cocineros

# Para ASIGNAR COCINERO se debe CAMBIAR informacion del cocinero.
#REQUERIRA: nombre del cocinero, estado y orden.
def asignar_cocinero(cocineros, orden):
    for cocinero in cocineros:
        if cocinero["Estado"] == "Libre":
            cocinero_asignado = {
                "Cocinero": cocinero["Cocinero"],
                "Estado": "Ocupado",
                "Orden": orden["Orden"],                
            }
            cocinero.update(cocinero_asignado)
            return cocinero
    return None

def hacer_orden(cocineros, orden):
    print(f" La orden {orden['Orden']} fue mandada a cocina, en espera de ser tomada...")
    time.sleep(5)      
    #El mesero debera ponerse en estado EN ESPERA
    cocinero_asignado = asignar_cocinero(cocineros, orden)
    if cocinero_asignado:
        #El cocinero queda OCUPADO y con los demas datos
        print(f" La orden {orden['Orden']} fue tomada por {cocinero_asignado['Cocinero']} \n      Preparando platillo...")
        time.sleep(5)    
        print("          Platillo listo!")
        #El cocinero debera ponerse en estado libre y sin orden tomada, y el mesero en OCUPADO
    else:
        print("No es posible generar el platillo")
    return None

# Tras obtener el platillo, el mesero se dirije a la mesa y se le entrega la orden se esperan 10 seg en comer, tras terminar el platillo, 
# el mesero retira los platos y esta en estado LIBRE, se ASIGNA uno de LIMPIEZA, se encargaran en limpiar la mesa por 10 seg, la mesa y orden
# vuelve a estar LIBRE y con datos predeterminados
    
# Para GESTIONAR LIMPIEZA se debe COMPROBAR el estado "LIBRE".
#REQUERIRA: nombre del conserje, estado y numero de mesa
def gestionar_conserje(limpieza):
    inf_conserje = []
    for conserje in limpieza:
        conserje = {
            "Conserje": conserje,
            "Estado": "Libre",
            "Mesa": 0,   
        }
        inf_conserje.append(conserje)
    return inf_conserje

# Para ASIGNAR LIMPIADOR se debe CAMBIAR informacion del conserje.
#REQUERIRA: nombre del conserje, estado y numero de mesa.
def asignar_conserje(limpieza, mesa):
    for conserje in limpieza:
        if conserje["Estado"] == "Libre":
            conserje_asignado = {
                "Conserje": conserje["Conserje"],
                "Estado": "Ocupado",
                "Mesa": mesa["Mesa"],                
            }
            conserje.update(conserje_asignado)
            return conserje
    return None

def entregar_orden(mesa, orden, mesero, limpieza):
    print(f" El mesero toma la orden {orden['Orden']} lista, se dirige a la mesa {mesa['Mesa']}")
    time.sleep(5)
    print(f" Los platillos son entregados en la mesa {mesa['Mesa']}, proceden a ingerir los alimentos...")
    time.sleep(10)
    print(" Los platillos son terminados, se retiran los comensales.")
    #La orden queda LIBRE y sin los demas datos
    time.sleep(5)
    print(f" El mesero {mesero['Mesero']} retira los platillos y se dirige a la cocina.")
    #El mesero queda LIBRE y sin los demas datos

    limpieza_asignada = asignar_conserje(limpieza, mesa)
    if limpieza_asignada:
        #La limpieza queda OCUPADA y con mesa
        print(f" El encargado de limpieza de la mesa {mesa['Mesa']} es {limpieza_asignada['Conserje']}")
        #La limpieza queda LIBRE y sin mesa
        time.sleep(6)
        print(f"             La mesa {mesa['Mesa']} queda libre.")
        #La mesa queda LIBRE y sin demas datos
    else:
        print("No hay de limpieza disponibles, mesa queda en espera")

def cargar_informacion(mesas, meseros, ordenes, cocineros, limpieza):
    try:
        with open("mesas.json", "r") as f:
            mesas = json.load(f)
        with open("meseros.json", "r") as f:
            meseros = json.load(f)
        with open("ordenes.json", "r") as f:
            ordenes = json.load(f)
        with open("cocineros.json", "r") as f:
            cocineros = json.load(f)
        with open("limpieza.json", "r") as f:
            limpieza = json.load(f)
    except Exception as e:        
        print("")
    
    info = atender_cliente(mesas, meseros, ordenes)
    hacer_orden(cocineros, info[2])   
    entregar_orden(info[0], info[2], info[1], limpieza)    
    guardar_informacion(mesas, meseros, ordenes, cocineros, limpieza)

if __name__ == "__main__":
    estados = ["Libre", "Ocupado", "En espera"]
    lista_mesas = [1, 2, 3, 4, 5]
    lista_ordenes = [223, 443, 43, 122, 553]
    lista_meseros = ["German", "Damian", "Martin", "Luis"]
    lista_cocineros = ["Daniel", "Miguel", "Oziel"]
    lista_limpieza = ["Joaquin", "Rodrigo"]
    gerente = ["Jhonny"]

    mesas = gestionar_mesa(lista_mesas)
    meseros = gestionar_mesero(lista_meseros)
    ordenes = gestionar_orden(lista_ordenes)
    cocineros = gestionar_cocinero(lista_cocineros) 
    limpieza = gestionar_conserje(lista_limpieza)

    cargar_informacion(mesas, meseros, ordenes, cocineros, limpieza)