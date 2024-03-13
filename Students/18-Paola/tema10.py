def meseros (lista_meseros):
    meseros_libres  = []
    for mesero in lista_meseros:
        dicMeseros = {
            "Nombre mesero ": mesero,
            "Mesa": 0,
            "Estado": "Libre"
        }
        meseros_libres.append(dicMeseros)
    return meseros_libres


def cocineros (lista_cocineros):
    cocineros_libres = []
    for cocinero in lista_cocineros:
        dicCocineros = {
            "Nombre cocinero": cocinero,
            "Orden":0,
            "Estado": "Libre"
        }
        cocineros_libres.append(dicCocineros)
        return cocineros_libres



def limpieza(lista_limpieza):
    limpieza_libres = []
    for limpiador in lista_limpieza:
        dicLimpiadores ={
            "Nombre limpiador": limpiador,
            "Estado": "Libre"
        }
def mesas()
def ordenes ()

if __name__ == "__main__":
  estados = ["Libre", "Ocupado", "En espera"]
  lista_mesas = [1,2,3,4,5]
  lista_ordenes = [223, 443, 43, 122,553]

  lista_meseros = ["German", "Damian", "Martin", "Juventino"]
  lista_cocineros = ["Daniel", "Miguel", "Oziel"]
  lista_limpieza = ["Joaquin", "Rodrigo"]
  gerente = ["Jhonny"]