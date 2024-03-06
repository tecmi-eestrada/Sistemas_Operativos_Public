#Clase con atributos y metodos que me identifican
class Frida():
    #Atributos
    def __init__(self, nombre, apellido, edad, color_favorito, comida_favorita, pasatiempo):
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad
        self.color_favorito = color_favorito
        self.comida_favorita = comida_favorita
        self.pasatiempo = pasatiempo

    #Metodos
    def pasatiempos(self):
        print(f"Mi pasatiempo favorito es {self.pasatiempo} junto a escuchar musica de diversos generos")

    def salir_con_amigos(self):
        print("Me gusta salir con mis amigos a diversos lugares y pasar tiempos agradables con ellos.")
    
    def quien_soy(self):
        print(f"Hola, mi nombre es {self.nombre} {self.apellido} y tengo {self.edad} años.")
        print(f"Mi color favorito es {self.color_favorito} y mi comida favorita son los {self.comida_favorita}.")

Yo_soy = Frida("Frida", "Garza", 17,"Morado", "Mariscos", "Leer")

Yo_soy.quien_soy()
Yo_soy.salir_con_amigos()
Yo_soy.pasatiempos()
