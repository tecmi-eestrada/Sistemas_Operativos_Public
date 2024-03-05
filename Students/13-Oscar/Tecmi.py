'''
Restaurante- Clase
(Nombre, tipo_de_comida, fundacion, mascota)

#instancia de la clase Restaurante
fondita-magica= Restaurante("Fondita_Magica", "antojitos_mexicanos", 1988, "Flautin")
'''
class Restaurante:
    def __init__(self, Nombre, tipo_de_comida, fundacion, mascota):
        self.Nombre = Nombre
        self.tipo_de_comida = tipo_de_comida
        self.fundacion = fundacion
        self.mascota = mascota
        
        #instancia de la clase Restaurante
fondita_magica = Restaurante("Fondita_Magica", "antojitos_mexicanos", 1988, "Flautin")
        

'''
Empleados - clase
(nombre, edad, departamento, rol)
'''
class Empleados:
    def __init__(self, nombre, edad, departamento, rol):
        self.nombre = nombre
        self.edad = edad
        self.departamento = departamento
        self.rol = rol
        



'''
gerente = Empleados("Rodrigo", 56, "Administrativo", "Gerente")


Gerente
   -Jefe de cocina
      -cocinero 1
      -cocinero 2
      -cocinero 3
   
   -Jefe de meseros
       - Mesero 1 
       - Mesero 2
       - Mesero 3
    
    -Jefe de Limpieza
       - Limpieza 1
       - Limpieza 2
       - Limpieza 3 
    
    -Otros
       -Cajero
       -Recepcionista
       -Barista        
'''