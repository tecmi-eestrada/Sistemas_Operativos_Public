LIBRE = 0
EN_ESPERA = 1
OCUPADO = 2

class Restaurante:
    def __init__(Self, Nombre, Orden, state):
        Self.Nombre = Nombre
        Self.Orden = Orden
        Self.state = state



def registro_de_estado(state):
    if state == LIBRE:
        print ("Libre")
        return state
    elif state == EN_ESPERA:
        print ("En espera")
        return state
    elif state == OCUPADO:
        print ("Ocupado")
        return state 
    
def registro_de_control(process, state):
    my_state = registro_de_estado(state)
    if state == LIBRE:
        print(f"El mesero esta libre {process}, state: {state}")
        return 0
    if state == EN_ESPERA:
        print(f"El mesero esta en espera  {process}, state: {state}")
        return 1
    if state == OCUPADO:
        print(f"El mesero esta ocupado {process}, state: {state}")
        return 2
    pass

def registro_de_datos(data, state, process):
    control = registro_de_control(process, state)
    if control == 1:
        print(f"Se le informo al {data}")
    if control == 0:
        print(f"Se le informo al {data}")
    if control == 2:
        print(f"Se le informo al {data}")


if __name__ == "__main__":
        estados = ["libre", "ocupado", "En espera"]

        lista_mesas = [1, 2, 3, 4, 5]
        lista_de_ordenes = [223, 443, 43, 122, 553]

        lista_meseros = ["German", "Damian", "Martin", "Juventino"]
        lista_cocineros = ["Daniel", "Miguel", "Oziel"]
        lista_limpieza = ["Juaquin", "Rodrigo"]
        gerente = ["Jhommy"]
        
        mi_tarea = "Supervisor"
        x = registro_de_datos(mi_tarea, OCUPADO, "")
        
        if x == OCUPADO:
            print (lista_meseros[1],"atendio a la mesa" , lista_mesas[2], "con numero de pedido",  lista_de_ordenes[3])
        if x == LIBRE:
            print (lista_meseros[1],"atendio a la mesa" , lista_mesas[2], "y se encuentra libre")
        if x == EN_ESPERA:
            print(lista_meseros[1],"atendio a la mesa" , lista_mesas[2], "y se encuentra en espera del pedido")

