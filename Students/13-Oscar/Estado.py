#Estado de un cocinero

Estado_Cocinando = 0
Estado_Libre = 1
Estado_Descanso = 2

def registro_de_estados (state):
    if state == Estado_Cocinando:
        print ("Cocinando")
        return state 
    elif state == Estado_Libre:
        print ("Cocinando")
        return state
    elif state == Estado_Descanso:
        print ("Limpiando")
        return state
    
def registro_de_control (process, state):
    my_state = registro_de_estados (state)
    if state == Estado_Cocinando:
        print (f"El cocinero esta ocupado, no disponible para {process}, estado: {my_state}")
        return 0
    if state == Estado_Libre:
        print (f"El cocinero esta libre, puede ayudar en {process}, estado: {my_state}")
        return 1
    if state == Estado_Descanso:
       print (f"No disponible, no molestar para {process}, estado: {my_state}")
       return 2
    pass

def registro_de_datos (data, state, process):
    control = registro_de_control(process, state)
    if control == 1:
     print(f"Dato enviado {data}")
    if control == 0:
        print("La tarea esta en espera") 
    if control == 2:
        print ("La tarea esta en proceso")   
        
if __name__ == "__main__":
    mi_tarea = "limpiar el piso" 
    registro_de_datos(mi_tarea, Estado_Libre, "enviar")      
 