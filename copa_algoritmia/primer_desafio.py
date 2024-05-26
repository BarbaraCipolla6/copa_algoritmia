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

    australia = {'Australia': australia_pases}
    argentina = {'Argentina': argentina_pases}

    print([australia, argentina])

def initPenales():
    print("\nEl partido ha empatado, empiezan los penales!")
    print("Abajo se encuentran las zonas del arco, elige hacia cual tirar para Argentina!")
    print(f"Argentina: 0 Paises Bajos: 0\n")
    print("[1, 2, 3]\n[4, 5, 6]\n[7, 8, 9,]\n")


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