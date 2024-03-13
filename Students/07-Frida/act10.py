#Gestionar meseros (nombre del mesero, mesa, orden, estado)
def gestion_meseros(meseros):
    meseros_turno = []
    for mesero in meseros:
        inf_mesero = {
            "Mesero": mesero,
            "Mesa": 0,
            "Orden": 0,
            "Estado": "Libre" 
        }
        meseros_turno.append(inf_mesero)
    return meseros_turno

#Funcion que asigne a un mesero dependiendo su estado a una mesa disponible y orden
def asignar_mesero(meseros, mesa, orden):
    for mesero in meseros:
        if mesero["Estado"] == "Libre":
            mesero_asignado = {
                "Mesero": mesero["Mesero"],
                "Mesa": mesa,
                "Orden": orden,
                "Estado": "Ocupado"
            }
            mesero.update(mesero_asignado)
            return mesero
    return None

#Gestionar cocineros (nombre del cocinero, estado, orden)
def gestion_cocineros(cocineros):
    cocineros_turno = []
    for cocinero in cocineros:
        inf_cocinero = {
            "Cocinero": cocinero,
            "Estado": "Libre",
            "Orden": 0
        }
        cocineros_turno.append(inf_cocinero)
    return cocineros_turno

#Funcion que asigne a un cocinero dependiendo su estado a una orden
def asignar_cocinero(cocineros, orden):
    for cocinero in cocineros:
        if cocinero["Estado"] == "Libre":
            cocinero_asignado = {
                "Cocinero": cocinero["Cocinero"],
                "Estado": "Ocupado",
                "Orden": orden
            }
            cocinero.update(cocinero_asignado)
            return cocinero
    return None

#Gestionar mesas (numero de mesa, estado, orden)
def gestion_mesas(mesas):
    mesas_dis = []
    for mesa in mesas:
        inf_mesa = {
            "Mesa": mesa,
            "Estado": "Libre",
            "Orden": 0
        }
        mesas_dis.append(inf_mesa)
    return mesas_dis

#Funcion que asigne a una mesa su estado y su orden
def asignar_mesa(mesas, orden):
    for mesa in mesas:
        if mesa["Estado"] == "Libre":
            mesa_asignada = {
                "Mesa": mesa["Mesa"],
                "Estado": "Ocupado",
                "Orden": orden
            }
            mesa.update(mesa_asignada)
            return mesa
    return None

#Funcion que asigne todos las funciones en una sola
def gestionar(meseros, ordenes, cocineros, mesas):
    for orden in ordenes:
        mesero = asignar_mesero(meseros, mesas, orden)
        if mesero:
            mesa = asignar_mesa(mesas, orden)
            if mesa:
                cocinero = asignar_cocinero(cocineros, orden)
                if cocinero:
                    print(f"Mesa asiganda: {mesa['Mesa']}")
                    print(f"Numero de orden: {orden}")
                    print(f"Mesero {mesero['Mesero']} asignado.")
                    print(f"Cocinero {cocinero['Cocinero']} asignado.")
                else:
                    print(f"No hay cocineros disponibles para la orden {orden}.")
                    mesa["Estado"] = "Libre"
                    mesero["Estado"] = "Libre"
            else:
                print(f"No hay mesas disponibles para la orden {orden}.")
                mesero["Estado"] = "Libre"
        else:
            print(f"No hay meseros disponibles para la orden {orden}.")

if __name__ == "__main__":
    #lista_meseros = ["German", "Damian", "Martin", "Luis"]
    #lista_mesas = [1, 2, 3, 4, 5]
    #lista_ordenes = [223, 443, 43, 122, 553]
    #lista_cocineros = ["Daniel", "Miguel", "Oziel"]
    #gerente = ["Jhonny"]
    
    estados = ["Libre", "Ocupado", "En espera"]
    lista_meseros = [
        {"Mesero": "German", "Estado": "Ocupado"}, 
        {"Mesero": "Damian", "Estado": "En espera"}, 
        {"Mesero": "Martin", "Estado": "Ocupado"}, 
        {"Mesero": "Luis", "Estado": "Libre"}
        ]
    lista_mesas = [
        {"Mesa": 1, "Estado": "Libre"}, 
        {"Mesa": 2, "Estado": "Libre"}, 
        {"Mesa": 3, "Estado": "Ocupada"}, 
        {"Mesa": 4, "Estado": "Libre"}, 
        {"Mesa": 5, "Estado": "En espera"}]
    lista_ordenes = [223, 443, 43, 122, 553]    
    lista_cocineros = [
        {"Cocinero": "Daniel", "Estado": "Libre"}, 
        {"Cocinero": "Miguel", "Estado": "Libre"}, 
        {"Cocinero": "Oziel", "Estado": "Libre"}
        ]

    gestionar(lista_meseros, lista_ordenes, lista_cocineros, lista_mesas)