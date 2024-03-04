from multiprocessing import Pool
import time

lista_actividades = (["Actividad_1", 30], ["Actividad_2", 6], ["Actividad_3", 16], ["Actividad_4", 4],
        ["Actividad_5", 2], ["Actividad_6", 2], ["Actividad_7", 12], ["Actividad_8", 3])


def logeo_de_trabajo(data):
    print(f"El Proceso {data[0]} esperara {data[1]} segundos")
    time.sleep(int(data[1]))
    print(f"El Proceso {data[0]} ha finalizado.")


def pool_handler():
    p = Pool(3)
    p.map(logeo_de_trabajo, lista_actividades)


if __name__ == '__main__':
    pool_handler()