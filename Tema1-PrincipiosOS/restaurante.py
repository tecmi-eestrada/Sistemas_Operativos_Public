'''
Restaurante - Clase
    (nombre, tipo_de_comida, fundacion, mascota)
    fondita_magica = Restaurante("Fondita Magica", "Antojitos Mexicanos", 1988, "Flautin")
'''
'''
    Empleados - Clase
        (nombre, edad, departamento, rol)
    #Instancias de la Clase Empleado
    gerente = Empleados("Rodrigo", 56, "Administrativo", "Gerente")
    jefe_de_cocina = Empleados("Rodrigo", 56, "Administrativo", "Jefe de Cocina")
    cocinero_1 = Empleados("Rodrigo", 56, "Administrativo", "Cocinero")
'''
'''
Gerente
    -Jefe de Cocina
         -Cocinero 1
         -Cocinero 2
         -Cocinero 3
    -Jefe de Meseros 
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
class Restaurante:
    def __init__(self, nombre, tipo_comida, fundacion, mascota):
        self.nombre = nombre
        self.tipo_comida = tipo_comida
        self.fundacion = fundacion
        self.mascota = mascota

    def contar_empleados(self, lista_empleados):
        numero_empleados = 0
        for i, empleado in enumerate(lista_empleados):
            print(f"Hola, soy el empleado {empleado.nombre}")
            numero_empleados = i + 1
        return numero_empleados


#Instancia de la Clase Restaurante
fondita_magica = Restaurante("Fondita Magica", "Antojitos Mexicanos", 1998, "Flautin")


class Empleados:
    def __init__(self, nombre, edad, departamento, rol):
        self.nombre = nombre
        self.edad = edad
        self.departamento = departamento
        self.rol = rol

gerente = Empleados("Rodrigo", 56, "Administrativo", "Gerente")
jefe_de_cocina = Empleados("Rodrigo", 56, "Administrativo", "Jefe de Cocina")
cocinero_1 = Empleados("Rodrigo", 56, "Administrativo", "Cocinero")
empleados = [gerente, jefe_de_cocina, cocinero_1]

print(fondita_magica.contar_empleados(empleados))
