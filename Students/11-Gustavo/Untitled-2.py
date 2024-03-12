HACIENDO_INVENTARIO = 1
DESCANSANDO = 2
ATENDIENDO_GENTE = 3

def registro_de_estado(state):
    if state == HACIENDO_INVENTARIO:
       print("Haciendo_inventario")
       return state
    elif state == DESCANSANDO:
        print("Descansando")
        return state
    elif state == ATENDIENDO_GENTE:
        print("atendiendo_gente")
        return state
    


def registro_de_control(process,state):
    my_state = registro_de_estado(state)
    if state == HACIENDO_INVENTARIO:
        print(f"Not in process, not able to {process}, state: {state}")
        return 1
    if state == DESCANSANDO:
        print(f"hold, not able to {process}, state: {state}")
        return 2
    pass

def registro_de_datos(data, state, process):
    control = registro_de_control(process, state)
    if control == 1:
        print(f"Data will be be sent {data}")
    if control == 0:
        print(f"Data will be hold {data}") 
    if control == 2:
        print(f"Data will be process {data}")

if __name__ == "__main__":
 mi_tarea = "Email"
registro_de_datos(mi_tarea, HACIENDO_INVENTARIO, "")

