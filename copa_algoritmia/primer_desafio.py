# Se importa el módulo random para usarlo próximamente.
import random

# Se crean dos listas con cada equipo y dentro se encuentran varias tuplas con los datos solicitados, este tipo de colección se utiliza para evitar la modificación de los mismos.
equipo_argentino = [("Sofía Toccalino", 2),
                    ("Agustina Gorzelany", 3),
                    ("Valentina Raposo", 4),
                    ("Agostina Alonso", 5),
                    ("María Forcherio", 6),
                    ("Agustina Albertarrio", 7),
                    ("María José Granatto", 10),
                    ("Delfina Thome", 11),
                    ("Cristina Cosentino", 13),
                    ("Clara Barberi", 14)
                    ]

equipo_australiano = [("Claire Colwill", 1), 
                    ("Ambrosia Malone", 2), 
                    ("Brooke Peris", 3), 
                    ("Amy Lawton", 4), 
                    ("Grace Young", 5), 
                    ("Penny Squibb", 6), 
                    ("Aleisha Power", 7), 
                    ("Wilson Georgia", 8), 
                    ("Shanea Tonkin", 9), 
                    ("Maddy Fitzpatrick", 10)
                    ]

# Mediante una función que tome los datos de cada equipo como parámetro se implementa el método choice con las dos opciones posibles, según cada opción se toma cada valor individual que contengan las tuplas de cada equipo. Luego del condional, se asignan los valores de los pases y del tiempo de manera aleatoria dentro de listas y finalmente la función devuelve el valor de lo requerido.  
def pases():
    equipo = random.choice(["Argentina", "Australia"])
    if equipo == "Argentina":
        nombre, camiseta = random.choice(equipo_argentino)
    else:
        nombre, camiseta = random.choice(equipo_australiano)

    posible_pase = random.choice([0,1])
    tiempo_partido = random.randint(1, 60)
    res_string = f"{equipo};{camiseta};{nombre};{posible_pase};{tiempo_partido}"

    return res_string

# Contar los pases buenos y malos para cada jugador
def contarPases(eventos):
    australia_pases = []
    argentina_pases = []

    jugadores_visto = []

    for evento in eventos:
        arr = evento.split(';')
        equipo = arr[0]
        camiseta = arr[1]
        nombre = arr[2]
        posible_pase = arr[3]

        # Si no tenemos un record de esta jugadora, crear un diccionario nuevo con sus datos
        visto = nombre in jugadores_visto
        if not visto:
            jugadores_visto.append(nombre)

            pases_bien = 0
            pases_mal = 0

            if posible_pase == '1':
                pases_bien = 1
            if posible_pase == '0':
                pases_mal = 1

            porcentaje = (pases_bien / 1) * 100

            jugador_dict = {
            'numero': camiseta,
            'nombre': nombre, 
            'cantidad_pases': 1,
            'pases_bien': pases_bien, 
            'pases_mal': pases_mal, 
            'porcentaje': '{:.2f}'.format(porcentaje)
            }
        
            if equipo == 'Australia':
                australia_pases.append(jugador_dict)
            elif equipo == 'Argentina':
                argentina_pases.append(jugador_dict)

        # Si tenemos un record de esta jugadora, encontramos su diccionario y actualizamos sus datos
        if visto:
            if equipo == 'Australia':
                for dict in australia_pases:
                    if dict['nombre'] == nombre:
                        cantidad_pases = dict['cantidad_pases'] + 1
                        pases_bien = dict['pases_bien']
                        pases_mal = dict['pases_mal']
                        porcentaje = dict['porcentaje']

                        if posible_pase == '1':
                            pases_bien += 1
                        elif posible_pase == '0':
                            pases_mal += 1

                        porcentaje = (pases_bien / cantidad_pases) * 100

                        dict.update({'cantidad_pases': cantidad_pases, 
                                     'pases_bien': pases_bien,
                                     'pases_mal': pases_mal,
                                     'porcentaje': '{:.2f}'.format(porcentaje)
                                     })
            elif equipo == 'Argentina':
                for dict in argentina_pases:
                    if dict['nombre'] == nombre:
                        cantidad_pases = dict['cantidad_pases'] + 1
                        pases_bien = dict['pases_bien']
                        pases_mal = dict['pases_mal']
                        porcentaje = dict['porcentaje']

                        if posible_pase == '1':
                            pases_bien += 1
                        elif posible_pase == '0':
                            pases_mal += 1

                        porcentaje = (pases_bien / cantidad_pases) * 100
                        
                        dict.update({'cantidad_pases': cantidad_pases, 
                                     'pases_bien': pases_bien,
                                     'pases_mal': pases_mal,
                                     'porcentaje': '{:.2f}'.format(porcentaje)
                                     })
    australia_pases.sort(key=lambda x: x['porcentaje'], reverse=True)
    argentina_pases.sort(key=lambda x: x['porcentaje'], reverse=True)

    australia = {'Australia': australia_pases}
    argentina = {'Argentina': argentina_pases}

    print([australia, argentina])
    

    

# Iniciamos el juego de penales
def initPenales():
    turno = "ARG"
    turno_cont = 0
    turno_cont_arg = 0
    turno_cont_pb = 0
    puntos_arg = 0
    puntos_pb = 0
    ganador = None
    final = False
    empatados = False
    input_valido = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
    arco_centro = ["2", "5", "8",]

    print("\nEl partido ha empatado, empiezan los penales!")
    print("Verás las zonas del arco, elige hacia cual tirar o atajar para Argentina!")
    print(f"Argentina: {str(puntos_arg)} Países Bajos: {str(puntos_pb)}\n")

    # Defenimos las funciones para manejar cada accion de juego - de jugador y de PB
    def tirar():
        nonlocal puntos_arg
        nonlocal turno
        nonlocal turno_cont
        nonlocal turno_cont_arg
        nonlocal empatados
        print("Tirarás para Argentina. Las zonas del arco se encuentran abajo.")
        print("Cuidado tirando hacia el centro, es más facil atajar ahi.\n")
        print("[1 2 3]\n[4 5 6]\n[7 8 9]\n")
        zonaArg = input("Ingresar el numero de zona: ")
        if zonaArg in input_valido:
            print(f"\nHas elegido tirar hacia la zona {zonaArg}!\n")
            resPB = random.randint(1, 9)

            if zonaArg in arco_centro and str(resPB) in arco_centro:
                print("Países Bajos ha atajado el tiro!")
                print(f"Argentina: {str(puntos_arg)} Países Bajos: {str(puntos_pb)}\n")
            elif zonaArg == str(resPB):
                print("Países Bajos ha atajado el tiro!")
                print(f"Argentina: {str(puntos_arg)} Países Bajos: {str(puntos_pb)}\n")
            elif zonaArg != str(resPB):
                print("Gollllll Argentina!!!!!")
                puntos_arg += 1
                print(f"Argentina: {str(puntos_arg)} Países Bajos: {str(puntos_pb)}\n")
        else:
            print("\nError: Ingresar el numero de zona (1-9)\n")
        
        turno = "PB"
        turno_cont += 1
        turno_cont_arg += 1
        if empatados == False:
            print(f"Intentos Argentina: {turno_cont_arg}/5")

        validarPuntos()

    def atajar():
        nonlocal puntos_pb
        nonlocal turno
        nonlocal turno_cont
        nonlocal turno_cont_pb
        nonlocal empatados
        print("Intentarás atajar para Argentina. Las zonas del arco se encuentran abajo.\n")
        print("[1 2 3]\n[4 5 6]\n[7 8 9]\n")
        zonaArg = input("Ingresar el numero de zona: ")
        if zonaArg in input_valido:
            print(f"\nHas elegido atajar la zona {zonaArg}!\n")
            resPB = random.randint(1, 9)

            if zonaArg in arco_centro and str(resPB) in arco_centro:
                print("Argentina ha atajado el tiro!")
                print(f"Argentina: {str(puntos_arg)} Países Bajos: {str(puntos_pb)}\n")
            elif zonaArg == str(resPB):
                print("Argentina ha atajado el tiro!")
                print(f"Argentina: {str(puntos_arg)} Países Bajos: {str(puntos_pb)}\n")
            elif zonaArg != str(resPB):
                print("Gollllll Países Bajos!!!!!")
                puntos_pb += 1
                print(f"Argentina: {str(puntos_arg)} Países Bajos: {str(puntos_pb)}\n")
        else:
            print("\nError: Ingresar el numero de zona (1-9)\n")

        turno = "ARG"
        turno_cont += 1
        turno_cont_pb += 1
        if empatados == False:
            print(f"Intentos Países Bajos: {turno_cont_pb}/5")
        
        validarPuntos()

    # Validamos si un equipo ha ganado
    def validarPuntos():
        nonlocal final
        nonlocal ganador
        nonlocal empatados

        if turno_cont >= 6 and puntos_arg - puntos_pb >= 3:
            final = True
            ganador = "ARG"
        elif turno_cont >= 6 and puntos_pb - puntos_arg >= 3:
            final = True
            ganador = "PB"

        if turno_cont >= 8 and puntos_arg - puntos_pb >= 2:
            final = True
            ganador = "ARG"
        elif turno_cont >= 8 and puntos_pb - puntos_arg >= 2:
            final = True
            ganador = "PB"

        if turno_cont == 10 and puntos_arg > puntos_pb:
            final = True
            ganador = "ARG"
        elif turno_cont == 10 and puntos_pb > puntos_arg:
            final = True
            ganador = "PB"
        elif turno_cont == 10 and puntos_arg == puntos_pb:
            final = True
            empatados = True
            print("Han empatado, desde ahora, el primer gol ganará!\n")

            puntuaje_arg = puntos_arg
            puntuaje_pb = puntos_pb

            # Bucle empatados (Ganar por primer gol)
            while empatados:
                if puntos_arg > puntuaje_arg:
                    ganador = "ARG"
                    break
                if puntos_pb > puntuaje_pb:
                    ganador = "PB"
                    break
                if turno == "ARG" and puntos_arg == puntuaje_arg and puntos_pb == puntuaje_pb:
                    tirar()
                if turno == "PB" and puntos_arg == puntuaje_arg and puntos_pb == puntuaje_pb:
                    atajar()

    # Bucle principal del juego
    while final == False:
        if turno == "ARG" and final == False:
            tirar()
        if turno == "PB" and final == False:
            atajar()

    # Bucle para validar el ganador
    while True:
        if ganador == "ARG":
            print("\nArgentina ha ganado!!!")
            print(f"Final: Argentina: {str(puntos_arg)} Países Bajos: {str(puntos_pb)}\n")
            break
        if ganador == "PB":
            print("\nPaíses Bajos ha ganado!!!")
            print(f"Final: Argentina: {str(puntos_arg)} Países Bajos: {str(puntos_pb)}\n")
            break

# Crear un nuevo archivo e escribir 50.000 eventos aleatorios
def crearArchivo():
    archivo_pases = open("pases.txt", "w", encoding='utf-8')        
    cont_pases = 0
    eventos = []

    while cont_pases < 50000:
        evento = pases()
        if cont_pases < 49999:
            eventos.append(f"{evento}\n")
        else:
            eventos.append(f"{evento}")
        cont_pases += 1

    contarPases(eventos)
    archivo_pases.writelines(eventos)

    initPenales()

# Ejecutar programa
if __name__ == "__main__":
    crearArchivo()