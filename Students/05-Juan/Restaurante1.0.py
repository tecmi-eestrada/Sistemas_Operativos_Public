# Gestion de Restaurante, cocineros, meseros, limpieza y gerente
import time

def mesas():
    pass

def ordenes():
    pass

def meseros():
    if len(lista_mesas) != 0:
        for numeroMesa in lista_mesas:
            estadoMesa = lista_mesas.get(numeroMesa)

    if len(lista_meseros) != 0:
        for nombreMesero in lista_meseros:
            estadoMesero = lista_meseros.get(nombreMesero)
            if estadoMesero == "En espera":
                print(f'El mesero {nombreMesero} esta {estadoMesero}')

                if len(lista_mesas) != 0:
                    for numeroMesa in lista_mesas:
                        estadoMesa = lista_mesas.get(numeroMesa)
                        print(f'El mesero {nombreMesero} esta atendiendo la mesa {numeroMesa}')
                        # Cambiar estado de mesero y de mesa
                        lista_meseros[nombreMesero] = "Ocupado"
                        lista_mesas[numeroMesa] = "Atendida"
                        # Esperar 5 segundos
                        time.sleep(5)
                        print(f'La mesa {numeroMesa} fue atendida')
                        lista_meseros[nombreMesero] = "En espera"
                        lista_mesas[numeroMesa] = "Libre"
                        break
                    break
    pass

def cocineros():
    if len(lista_ordenes) != 0:
        for numeroOrden in lista_ordenes:
            estadoOrden = lista_ordenes.get(numeroOrden)
            if estadoOrden == "En espera":
                print(f'la orden {numeroOrden} esta en {estadoOrden}')
                break

    if len(lista_cocineros) != 0:
        for nombreCocinero in lista_cocineros:
            estadoCocinero = lista_cocineros.get(nombreCocinero)
            if estadoCocinero == "En espera":
                print(f'El cocinero {nombreCocinero} esta haciendo la orden {numeroOrden}')
                # Cambiar estado de cocinero y de orden
                lista_cocineros[nombreCocinero] = "Ocupado"
                lista_ordenes[numeroOrden] = "En proceso"
                # Esperar 5 segundos
                time.sleep(5)
                print(f'La orden {numeroOrden} esta lista')
                lista_cocineros[nombreCocinero] = "En espera"
                lista_ordenes[numeroOrden] = "Lista"
                break
    pass

def limpieza():
    pass

if __name__ == "__main__":
    lista_mesas = {1:"Libre", 2:"Atendida", 3:"Ocupada", 4:"Libre", 5:"Libre"}
    lista_ordenes = {223:"En proceso", 433:"En espera", 43:"En espera", 122:"En espera", 553:"En espera"}

    lista_meseros = {"German":"En espera", "Damian":"Ocupado", "Martin":"En espera", "Juventino":"En espera"}
    lista_cocineros = {"Daniel":"Ocupado", "Miguel":"En espera", "Oziel":"En espera"}
    lista_limpieza = {"Joaquin":"En espera", "Rodrigo":"Ocupado"}
    gerente = {"Jhonny":"En espera"}

    cocineros()
    # mesas()
    # meseros()