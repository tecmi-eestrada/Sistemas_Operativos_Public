if __name__ == "__main__":
    estados = ["libre", "ocupado", "en espera"]
LIBRE = 1
OCUPADO = 2
EN_ESPERA = 3

def registro_de_estados(state):
    if state == LIBRE:
        print("LIBRE")
        return state
    elif state == OCUPADO:
        print("OCUPADO")
        return state
    elif state ==EN_ESPERA:
        print("EN ESPERA")
        return state
    

    lista_mesas = [1, 2, 3, 4, 5]
    lista_ordenes =[122, 232, 435, 545, 45]

    lista_meseros =["german", "damian", "jose", "ariel"]
    lista_cocineros = ["daniel", "miguel", "joaquin"]
    lista_limpieza = ["dan", "joss", "martin"]
    gerente =["jonny"]


def registro_de_control(process, state):
    my_state = registro_de_estados(state)
    if state == LIBRE:
        print(f"SU MESA ESTA SIENDO ATENDIDA")
        return 1
    if state == OCUPADO:
        print(f"no puede atender, esta ocupado {process}, estado {my_state}")
        return 2
    if state == EN_ESPERA:
        print(f"no puede atender, esta en descanso {process}, estado {my_state}")
        return 3
    
#funcion que gestiona meseros
def meseros():
     if state == LIBRE:
        print(f"puede atender, esta desocupado {process}, estado {state}")
        return 1
#funcion que gestiona cocineros
def cocineros():

#funcion que gestiona limpieza
def limpieza():

#funcion que gestiona mesas
def mesas():

#funcion que gestiona ordenes
def ordenes():








