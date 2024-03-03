import os #Libreria basica del sistema operativo
import time #Libreria para medir o realizar acciones con tiempo
import psutil #Libreria especifica de python para utilidades del sistema operativo
import json #Librearia para archivos json
import pandas as pd #Libreria pandas para gestion de datos en vectores y matrices
import pathlib #Librearia especifica de python para utilidades de directorios
import platform #Librearia especifica de python para propiedades del sistema (independiente del sistema operativo)

my_os = platform.system()
print("OS in my system : ", my_os)

# Contar numero de CPUs
# cpu_num = os.cpu_count()
# print(cpu_num)

# Obtener las variables de ambiente
# env_vars = os.environ
# print(env_vars)


# Añadir la nueva variable
# os.environ['VariableDePrueba'] = 'SoyVariable'

# Obtener valor de variable
# mi_os = os.getenv("OS")
# print(mi_os)

# Obtener la variable
# print("Mi variable es:", os.environ['VariableDePrueba'])

# Obtener diccionario actual
# mi_ruta = os.getcwd()
# print(mi_ruta)

# Obtener PID
# pid = os.getpid()
# print("PID del proceso ", pid)
# time.sleep(10)

# Obtener nombre proceso por pid
# pid = os.getpid()
# process = psutil.Process(pid)
# print(process)

# Imprimir los procesos mediante process_iter
# for proceso in psutil.process_iter():
#     mi_proceso = proceso.name()
#     id_proceso = proceso.pid
#     print(mi_proceso , ' ::: ', id_proceso)

# lista_de_procesos = list()
# # Iterate over all running processes
# for proceso in psutil.process_iter():
#    # Get process detail as dictionary
#    info_procesos = proceso.as_dict(attrs=['pid', 'name', 'cpu_percent'])
#    # Append dict of process detail in list
#    lista_de_procesos.append(info_procesos)

# # Crear archivos con pandas
# df = pd.DataFrame(lista_de_procesos)
# df.to_excel("output_files\procesos_pandas_excel.xlsx",sheet_name="procesos")
# df.to_json("output_files\procesos_pandas.json")
# # print(df)

# # Crear json con objeto texto
# with open("output_files\mis_procesos.json", 'a') as f:
#    json.dump(lista_de_procesos, f)