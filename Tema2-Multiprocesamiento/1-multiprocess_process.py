import multiprocessing
import time

# print("# CPU", multiprocessing.cpu_count())

def imprimir_proceso(proceso):
    print('Esta es la : ', proceso)

if __name__ == "__main__":  
    lista_acts = ["Actividad1", "Actividad2", "Actividad3", "Actividad4"]
    processes = []

    # instanciando el proceso con argumentos
    for process in lista_acts:
        proc = multiprocessing.Process(target=imprimir_proceso, args=(process,))
        processes.append(proc)
        proc.start()
        time.sleep(3)

    # finalizar los procesos
    for proc in processes:
        proc.join()
