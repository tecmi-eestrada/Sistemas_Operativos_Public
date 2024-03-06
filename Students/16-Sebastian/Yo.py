class Sebas:
    def __init__(self, nombre, apellido, edad, hobbie, personalidad):
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad
        self.hobbie = hobbie
        self.personalidad = personalidad

    def __str__(self):
        return f"Nombre: {self.nombre}, Apellido: {self.apellido}, Edad: {self.edad}, Hobbie: {self.hobbie}, Personalidad: {self.personalidad}"

    def jugar_videojuegos(self):
        print("Me gusta jugar videojuegos")

    def cocinar(self):
        print("Prefiero preparar la comida en lugar de pedir a domicilio")

    def ver_anime(self):
        print("Disfruto mucho de los animes")

yo = Sebas("Sebas", "Soria", 18, "jugar videojuegos", "introvertido")

print(yo)
yo.jugar_videojuegos()
yo.cocinar()
yo.ver_anime()