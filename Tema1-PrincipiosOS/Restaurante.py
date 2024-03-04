'''
            Restaurante - Clase
                    (nombre, tipo_comida, fundacion, mascota) <- ATRIBUTOS
                ~ Instancias de clase
                fondita = Restaurante("Fondita magica", "Antojitos Mexicanos", 1988, "Flautin")
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
            numero_empleados  = i + 1
        return numero_empleados    

fondita = Restaurante("Fondita magica", "Antojitos Mexicanos", 1988, "Flautin")

'''                   
                Empleados - Clase
                    (nombre, edad, departamento, rol) <- ATRIBUTOS
                ~ Instancias de clase
                gerente = Empleados("Rodrigo", 56, "Administrativo", "Gerente")
                jefe_cocina = Empleados("Rodrigo", 56, "Administrativo", "Jefe de Cocina")
                cocinero_1 = Empleados("Rodrigo", 56, "Administrativo", "Cocinero")
'''

class Empleados:
    def __init__(self, nombre, edad, departamento, rol):
        self.nombre = nombre
        self.edad = edad
        self.departamento = departamento
        self.rol = rol
        
gerente = Empleados("Rodrigo", 56, "Administrativo", "Gerente")
jefe_cocina = Empleados("Jesus", 42, "Administrativo", "Jefe de Cocina")
cocinero_1 = Empleados("Elias", 36, "Administrativo", "Cocinero")

empleados = [gerente, jefe_cocina,cocinero_1]

print(fondita.contar_empleados(empleados))

'''
    Gerente
        -Jefe de Cocina
            -Cocinero 1
            -Cocinero 2
            -Cocinero 3

        -Jefe de Meseros
            -Mesero 1
            -Mesero 2
            -Mesero 3
        
        -Jefe fr Limpieza
            -Limpieza 1
            -Limpieza 2
            -Limpieza 3
        
        -Otros
            -Cajero 
            -Recepcionista
            -Barista

'''


