#INACTIVE
TRABAJANDO =0
SIN_HACER_NADA =1
EN_DESCANSO =2

def registro_de_estados(state):
    if state == TRABAJANDO:
        print("trabajando")
        return state
    elif state == SIN_HACER_NADA:
        print("sin hacer nada")
        return state
    elif state ==EN_DESCANSO:
        print("en descanso")
        return state
    

def registro_de_control(process, state):
    my_state = registro_de_estados(state)
    if state == SIN_HACER_NADA:
        print(f"puede atender, esta desocupado {process}, estado {my_state}")
        return 0
    if state == TRABAJANDO:
        print(f"no puede atender, esta ocupado {process}, estado {my_state}")
        return 1
    if state == EN_DESCANSO:
        print(f"no puede atender, esta en descanso {process}, estado {my_state}")
        return 2

def registro_de_datos(data, state, process):
    control =registro_de_control(process, state)
    if control ==1:
        print(f"data will be sent {data}")
    if control ==0:
        print(f"data will be hold ")
    if control ==2:
        print(f"data will be process ")

if __name__ == "__main__":
    mi_mesero= "meserear"
    registro_de_datos(mi_mesero, SIN_HACER_NADA, "para tomar pedido")
 



