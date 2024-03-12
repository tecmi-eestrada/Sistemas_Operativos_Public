#ESTADOS 
SIN_TRABAJO = 0
CON_TRABAJO = 1
EN_ESPERA = 2

def registro_estados(estado):
    if estado == SIN_TRABAJO:
        print("                                    Sin trabajo")
        return estado
    elif estado == CON_TRABAJO:
        print("                                    Con trabajo")
        return estado
    elif estado == EN_ESPERA:
        print("                                    En descanso")
        return estado

def registro_control(proceso, estado):
    mi_estado = registro_estados(estado)
    if estado == SIN_TRABAJO:
        print(f"         El empleado no esta trabajando, el esta {proceso}, estado: {mi_estado} ")
        return 0
    if estado == CON_TRABAJO:
        print(f"         El empleado esta trabajando, el esta {proceso}, estado: {mi_estado}")
        return 1
    if estado == EN_ESPERA:
        print(f"                 El empleado esta en espera para {proceso}, estado: {mi_estado}")
        return 2
    pass

def registro_datos(empleado, estado, proceso):
    control = registro_control(proceso, estado)
    if control == 1:
        print(f"                         El empleado a tratar es {empleado}")
    if control == 0:
        print(f"                              {empleado} no esta trabajando")
    if control == 2:
        print("                        Empleado en espera de realizar trabajo")


if __name__ == "__main__":
    registro_datos("Cocinero", CON_TRABAJO, "preparando platillos")
    print("")
    registro_datos("Mesero", EN_ESPERA, "platillos")
    print("")
    registro_datos("Cajero", SIN_TRABAJO, "usando el celular")