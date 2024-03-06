class AlejandroGonzalez():
    nombre = "Alejandro"
    edad = 19
    estatura = 1.71
    personalidad = "Buena onda, extrovertido y hablador"
    def __init__(self, nombre=nombre, edad=edad, estatura=estatura, personalidad=personalidad) -> None:
        self.nombre = nombre
        self.edad = edad
        self.estatura = estatura
        self.personalidad = personalidad
        

    def print_all(self):
        print(f"Nombre del Estudiante: {self.nombre}")
        print(f"Edad: {self.edad} años")
        print(f"Estatura: {self.estatura} m")
        print(f"Personalidad: {self.personalidad}")

class Actividades:
    fav_1 = "ir al gym"
    fav_2 = "salir con amigos"
    fav_3 = "estudiar"
    fav_4 = "comer"

    def mis_acts(self):
        print("mis actividades favoritas son "+ self.fav_1 + self.fav_2 + self.fav_3+"  y tambien "+ self.fav_4)

alejandro = AlejandroGonzalez()
alejandro.print_all()

alejandro_acts = Actividades()
alejandro_acts.mis_acts()