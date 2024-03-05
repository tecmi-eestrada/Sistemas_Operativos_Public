'''
Restaurante - clase
  (nombre,  tipo_de_comida, fundación, mascota)<- Atributos
    
    #instancia de la clase restaurante
     fondita_magica = Restaurante("Fondita Magica", "Antojitos Mexicanos", 1988, "Flautin")
'''


'''

Empleados-class
(Nombre, Edad, Departamento, Rol)

Gerente = Empleados ("Rodrigo", 56, "Administrativo", "Gerente")
jefe_de-cocina = Empleados ("Rodrigo", 56, "Administrativo", "Jefe de cocina")
Cocinero_1 = Empleados ("Rodrigo", 56, "Administrativo" "Cocinero")
'''

'''

Restaurante 
Gerente
   -Jefe de Cocina
      -Cocinero 1
      -Cocinero 2
      -Cocinero 3 
   -Jefe de Meseros
      -Mesoro 1
      -Mesoro 2
      -Mesoro 3
   -Jefe de Limpieza
      -Limpieza 1
      -Limpieza 2
      -Limpieza 3
   -Otros
       -cajeros 
       -Recepcionista
       -Barista
'''
class Restaurante:
   def __init__(self, Nombre, Tipo_de_comida, Fundación, Ingredientes):
      self.Nombre=Nombre
      self.Tipo_de_comida=Tipo_de_comida
      self.Fundación=Fundación
      self.Ingredientes=Ingredientes

#instancia de la clase restaurante
      fondita_magica = Restaurante("Fondita Magica", "Antojitos Mexicanos", 1988, "Flautin")

      def contar_empleados(lista_empleados):
         for empleado in lista_empleados:
            print(f"Hola, soy el empleado" (empleado.nombre))




class persona:
   def __init__(self, Nombre, Departeamento, Edad, Rol):
      self.Nombre=Nombre
      self.Edad=Edad
      self.Departamento=Departeamento
      self.Rol=Rol

