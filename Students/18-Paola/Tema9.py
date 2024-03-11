#ESTADO
ESTADO_INACTIVO = 0
ESTADO_ACTIVO = 1
ESTADO_SUSPENDIDO = 2

def registro_de_estados(state):
    if state == ESTADO_INACTIVO:
        print("Inactivo")
        return state
    elif state == ESTADO_ACTIVO:
        print("Activo")
        return state
    elif state == ESTADO_SUSPENDIDO:
        print("Suspendido")
        return state
    
def registro_de_control (proceso,state):
    mi_state = registro_de_estados(state)
    if state == ESTADO_INACTIVO:
        print (f"El cocinero se encuentra ocupado en otra actividad, el no podra: {proceso}, su estado es : {mi_state}")
        return 0
    if state == ESTADO_ACTIVO:
        print (f"El cocinero esta disponible, el podra {proceso}, su estado es: {mi_state}")
        return 1
    if state == ESTADO_SUSPENDIDO:
        print (f"El cocinero esta descansando, el no podra {proceso}, su estado es: {mi_state}")
        return 2
    pass
    
def registro_de_datos(data, state, proceso):
    control = registro_de_control(proceso, state)
    if control == 0:
        print("Procesando, el empleado estara listo mas tarde")
    if control == 1:
        print(f"Procesando, el empleado podra: {data}")
    if control == 2:
        print("Procesando, el empleado esta en su hora de descanso")

if __name__ == "__main__":

    mi_tarea= "Cocinar"
    registro_de_datos(mi_tarea,ESTADO_SUSPENDIDO,"hacer platillos")