class Oscar:
    def __init__(self, nombre, color_cabello, estatura, edad):
    
     self.nombre = nombre
     self.color_cabello = color_cabello
     self.estatura = estatura
     self.edad = edad

    def jugarVideoJuegos(self):
     print("Una de mis actividades favoritas es jugar video juegos")


    def irAlGym(self):
      print ("mi actividad favorita es ir al gym todos los dias")

    def Programar(self):
      print("Una de mis actividades favoritas es practicar la programacion con el lenguaje de JavaScript")

yo = Oscar("oscar", "negro", 1.60, 22)

yo.irAlGym()
