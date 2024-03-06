class Luis():
    def __init__(self, nombre, apellido, musica, hobbies) -> None:
        self.apellido = apellido
        self.nombre = nombre
        self.musica_pref = musica
        self.hobbies_pref = hobbies

    def musica(self):
        return f"{self.musica_pref} y Rock"

    def hobbies(self):
        return "Videojuegos"

# Ejemplo de uso con print
luis = Luis(nombre="Luis", apellido="Apellido", musica="Rock", hobbies=["Valorant", "Computadora"])
print("Nombre: {luis.nombre}")
print(f"Apellido: {luis.apellido}")
print(f"Género musical preferido: luis.musica()")
print(f"Hobbies: luis.hobbies(), (luis.hobbies_pref)")