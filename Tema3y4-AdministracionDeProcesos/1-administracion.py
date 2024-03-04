from multiprocessing import Pool
import time

vehiculos_estacionados = []

def pago_parquimetro(nombre, edad):
    tiempo = int(input("Cuantos minutos planea pagar en el parquimetro? - "))
    my_string = f"{nombre.capitalize()} de {edad}"
    datos = (my_string, tiempo)
    return datos

def parking(num_vehiculos):
    for _ in range(num_vehiculos):
        print("Favor de llenar el formulario para solicitar tiempo de estacionamiento")
        nombre = input("Cual es su nombre? - ")
        edad = input("Cual es su edad? - ")
        registro = pago_parquimetro(nombre,edad)
        vehiculos_estacionados.append(registro)


def bitacora_de_vehiculos(vehiculos):
    print(f"El vehiculo de {vehiculos[0]} estara estacionado por {vehiculos[1]} minutos")
    time.sleep(int(vehiculos[1]))
    print(f"El vehiculo {vehiculos[0]} ha salido del estacionamiento.")

def valet_parking():
    p = Pool(2)
    p.map(bitacora_de_vehiculos, vehiculos_estacionados)


if __name__ == '__main__':
    my_iter = int(input("Cuantos vehiculos son? -"))
    parking(my_iter)
    print("\nEstacionando vehiculos")
    valet_parking()

