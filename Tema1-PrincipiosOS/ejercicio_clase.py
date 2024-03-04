'''
Restaurante - Clase
    (nombre, tipo_de_comida, fundacion, mascota) <- Atributos

    #Instancia de la Clase Restaurante
    fondita_magica = Restaurante("Fondita Magica", "Antojitos Mexicanos", 1988, "Flautin")
'''


class Restaurante:
    def __init__(self, nombre, tipo_de_comida, fundacion, mascota):
        self.nombre = nombre
        self.tipo_de_comida = tipo_de_comida
        self.fundacion = fundacion
        self.mascota = mascota

    def contar_empleados(self, lista_empleados):
        numero_empleados = 0
        for i, empleado in enumerate(lista_empleados):
            print(f"Hola, soy el empleado {empleado.nombre} y mi rol es {empleado.rol}")
            numero_empleados = i + 1
        return numero_empleados

# lista_estudiantes = ["estudiante1", "estudiante2", "estudiante3", "estudiante4"]
# print(len(lista_estudiantes))
# for idx, estudiante in enumerate(lista_estudiantes):
#     print(idx, estudiante)

#Instancia de la Clase Restaurante
fondita_magica = Restaurante("Fondita Magica", "Antojitos Mexicanos", 1988, "Flautin")

'''
    Empleados - Clase
        (nombre, edad, departamento, rol)  <- Atributos
    
    #Instancias de la Clase Empleado
    gerente = Empleados("Rodrigo", 56, "Administrativo", "Gerente")
    jefe_de_cocina = Empleados("Rodrigo", 56, "Administrativo", "Jefe de Cocina")
    cocinero_1 = Empleados("Rodrigo", 56, "Administrativo", "Cocinero")
'''
class Empleados:
    def __init__(self, nombre, edad, departamento, rol):
        self.nombre = nombre
        self.edad = edad
        self.departamento = departamento
        self.rol = rol

gerente = Empleados("Rodrigo", 56, "Administrativo", "Gerente")
jefe_de_cocina = Empleados("Ulises", 18, "Cocina", "Jefe de Cocina")
cocinero_1 = Empleados("Fabian", 22, "Cocina", "Cocinero")
empleados = [gerente, jefe_de_cocina, cocinero_1]


print(fondita_magica.contar_empleados(empleados))

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