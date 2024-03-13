            
mesa = ["1","En espera"]

meseros = ["Juan","Libre","Paco","Ocupado","Jose","Libre"]

def mostrar_meseros(meseros):
    contador = 0
    for elemento in meseros:
        if contador % 2 == 0 and contador != 0:
            print("\n")
        print(elemento)
        contador += 1
while True: 
    print ("------------------------------------")
    print ("            Restaurante             ")
    print ("------------------------------------")
    print ("1) Meseros Disponibles")
    print ("2) Supervision de mesas")
    print ("------------------------------------")
    seleccion = input("")
    if seleccion == "1":
        print ("El mesero",meseros[0],"esta",meseros [1])
        print ("Deseas regresar al menu? (si/no)")
        mes_s = input ("")
        if mes_s == "si":
            continue
        else:
            print ("Gracias por usar el programa")
            break

    if seleccion == "2":
        print("Selecciona la mesa que deseas atender:")
        print("1)La mesa", mesa[0], "esta", mesa[1])
        print("-Presiona M para regresar al menu")
        m_seleccion = input("")
        if m_seleccion == "1":
            if mesa[1] == "Siendo atendida":
                print ("La mesa esta siendo atendida")
            else:
                print ("Selecciona un mesero libre para atender la mesa:")
                mostrar_meseros(meseros)
