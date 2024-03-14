import time

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
def asignar_mesero(meseros, mesa):
    for mesero in meseros:
        if mesero["Estado"] == "Libre":
            mesero_asignada = {
                "Mesero": mesero["Mesero"],
                "Mesa": mesa["Mesa"],
                "Orden": 0,
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

# Se resguarda información de la mesa, mesero y orden. DUDA
# REQUERIRA: mesa, mesero y orden 

def antender_cliente(mesa,mesero,orden):
    mesa_asignada = asignar_mesa(mesa)
    print("Atendido a cliente, esperando para asignar mesa...")
    time.sleep(5)
    
    print(f"         Su mesa sera la {mesa_asignada['Mesa']}")
    time.sleep(10)

    mesero_asignado = asignar_mesero(mesero, mesa)
    print(f"      Su mesero sera {mesero_asignado['Mesero']}")
    time.sleep(5)

    orden_asignada = asignar_orden(orden, mesa_asignada, mesero_asignado)
    print(f"      Tomando orden {orden_asignada['Orden']} por {mesero_asignado['Mesero']}")
    time.sleep(15)

    return mesero_asignado, mesa_asignada, orden_asignada

# Tras hacer pedido, a la mesa se le asigna un cocinero LIBRE (toma 10 seg en asignar), se le pone en espera unos 20 seg para generar el platillo y
# el MESERO esta en ESPERA, mientras el COCINERO esta OCUPADO, finaliza la generación de platillo y se pone en estado LIBRE al cocinero

# Para GESTIONAR COCINERO se debe COMPROBAR el estado "LIBRE".
#REQUERIRA: nombre del cocinero, estado y orden
def gestionar_cocinero(cocineros):
    inf_cocinero = []
    for cocinero in cocineros:
        inf_cocinero = {
            "Cocinero": cocinero,
            "Estado": "Libre",
            "Orden": 0,   
        }
        inf_cocinero.append(inf_cocinero)
    return inf_cocinero

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
    print(f"La orden {orden['Orden']} fue mandada a cocina, en espera de ser tomada...")
    time.sleep(10)      
    cocinero_asignado = asignar_cocinero(cocineros, orden)

    print(f"La orden {orden['Orden']} fue tomada por {cocinero_asignado['Cocinero']} \n                 Preparando platillo...")
    time.sleep(20)    
    print("                        Platillo listo")

# Tras obtener el platillo, el mesero se dirije a la mesa y se le entrega la orden se esperan 10 seg en comer, tras terminar el platillo, 
# el mesero retira los platos y esta en estado LIBRE, se ASIGNA uno de LIMPIEZA, se encargaran en limpiar la mesa por 10 seg, la mesa y orden
# vuelve a estar LIBRE y con datos predeterminados

# Para GESTIONAR LIMPIEZA se debe COMPROBAR el estado "LIBRE".
#REQUERIRA: nombre del conserje, estado y numero de mesa
def gestionar_conserje(limpieza):
    inf_conserje = []
    for conserje in limpieza:
        inf_conserje = {
            "Conserje": conserje,
            "Estado": "Libre",
            "Mesa": 0,   
        }
        inf_conserje.append(inf_conserje)
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

def entregar_oden(mesa, orden, mesero, limpieza):
    print(f"El mesero toma la orden {orden['Orden']} lista, se dirige a la mesa {mesa['Mesa']}")
    time.sleep(5)
    print(f"Los platillos son entregados en la mesa {mesa['Mesa']}, proceden a ingerir los alimentos...")
    time.sleep(10)
    print("Los platillos son terminados, retirandose los comensales.")
    time.sleep(5)
    print(f"El mesero {mesero['Mesero']} retira los platillos y se dirige a la cocina.")

    limpieza_asignada = asignar_conserje(limpieza)
    print(f"      El encargado de limpieza de la mesa {mesa['Mesa']} es {limpieza_asignada['Conserje']}")
    time.sleep(6)