class JuanDescripcion():
    def __init__(self):
        self.nombre = "Juan"
        self.edad = 25
        self.altura = 1.75
        self.color_ojos = "Cafe"
        self.color_cabello = "Negro"
        
    def descripcion(self):
        print(f'Mi nombre es {self.nombre}, tengo {self.edad} años y mido {self.altura} metros')
        print(f'Mis ojos son color {self.color_ojos} y el color de mi cabello es {self.color_cabello} \n')
        
class JuanActividades():
    def actividades():
        actividades = [
            'Jugar Videojuegos',
            'Ver series y peliculas',
            'Hablar con mis amigos'
        ]
        
        print('Mis actividades favoritas son:')
        for i in actividades:
            print(f'- {i}')
        
claseDescripcion = JuanDescripcion()
claseDescripcion.descripcion()


JuanActividades.actividades()

