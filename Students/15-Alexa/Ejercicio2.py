#Class que me representa
class Alexa():
    
    #atributos que me hacen ser quien soy
    def __init__(self, nombre, edad, genero, color_favorito, hobbies) -> None:
        self.nombre = nombre
        self.edad = edad
        self.genero = genero
        self.color_favorito = color_favorito
        self.hobbies = hobbies
        
     #acciones favoritas
    def ir_al_gym(self):
         print("Mi actividad favorita es ir al gym")  
        
    def escuchar_musica(self):
         print("Mi actividad favorita es escuchar musica") 
         
    def ver_series(self):
         print("Mi actividad favorita es ver series") 