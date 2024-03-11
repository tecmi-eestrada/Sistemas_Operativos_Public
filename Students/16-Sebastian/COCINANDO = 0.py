COCINANDO = 0
LAVANDO = 1
DESCANSANDO = 2

def registro_de_estado(state):
    if state == COCINANDO:
        print ("Cocinando")
        return state
    elif state == LAVANDO:
        print ("lavando")
        return state
    elif state == DESCANSANDO:
        print ("Decansando")
        return state
    
def reistro_de_control(process, state):
    my_state = registro_de_estado(state)
    if state == COCINANDO:
        print(f"El cocinero esta prparando un platillo{process}, state: {state}")
        return 0
    if state == LAVANDO:
        print(f"El conciero esta lavando {process}, state: {state}")
        return 1
    if state == DESCANSANDO:
        print(f"El cocinero esta en descanso {process}, state: {state}")
        return 2
    pass
    
def registro_de_datos(data, state, process):
    control = reistro_de_control(process, state)
    if control == 1:
        print(f"Se le informo al {data}")
    if control == 0:
        print(f"Se le informo al {data}")
    if control == 2:
        print(f"Se le informo al {data}")
    
if __name__ == "__main__":
    mi_tarea = "Supervisor"
    registro_de_datos(mi_tarea, COCINANDO, "")

