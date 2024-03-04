'''
Restaurante - Class
    (Nombre, tipo_de_comida, fundacion, mascota)

    #Intancia de la clase
    fondita_magica = Restaurante ("Fondita magica", "Antojitos mexicanos", 1988, "Flautin")
'''
    


'''
    Empleados - Class
        (Nombre, Edad, Departamento, Rol)

        Gerente = Empleados ("Rodrigo", 56, "Administrativo", "Gerente")
        jefe_de_cocina = Empleados ("Rodrigo", 56, "Administrativo", "Jefe de cocina")
        Cocinero_1 = Empleados ("Rodrigo", 56, "Administrativo", "Cocinero")
'''



'''
Gerente
    -Jefe de cocina
        -Cocinero 1
        -Cocinero 2
        -Cocinero 3

    -Jefe de Meseros
        -Mesero 1
        -Mesero 2
        -Mesero 3

    -otros
        -Cajero
        -Recepcionista
        Barista
'''

class Restaurante:
    def __init__(Self, Nombre, tipo_de_comida, fundacion, mascota):
        Self.Nombre = Nombre
        Self.tipo_de_comida = tipo_de_comida
        Self.funacion = fundacion
        Self.mascota = mascota

#Intancia de la clase
fondita_magica = Restaurante ("Fondita magica", "Antojitos mexicanos", 1988, "Flautin")

def contar_empleado(lista_empleados):
    for i,  empleado in lista_empleados:
            print(f"Hola, soy el empleados (empleado.nombre) y mi rol es (empleado.rol)")
            numero_empleados = i + 1
    return numero_empleados



class Empleados:
    def __init__(Self, Nombre, Edad, Departamento, Rol):
        Self.Nombre = Nombre
        Self.Edad = Edad
        Self.Deparamento = Departamento
        Self.Rol = Rol

Gerente = Empleados ("Rodrigo", 34, "Administrativo", "Gerente")
jefe_de_cocina = Empleados ("Pepe", 23, "Cocina", "Jefe de cocina")
Cocinero_1 = Empleados ("Juan", 45, "Cocina", "Cocinero")
        