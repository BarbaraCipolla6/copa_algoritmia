# Se importa el módulo random para usarlo próximamente.
import random

# Mediante una función que tome los datos de cada equipo como parámetro se implementa el método choice con las dos opciones posibles, según cada opción se toma cada valor individual que contengan las tuplas de cada equipo. Luego del condional, se asignan los valores de los pases y del tiempo de manera aleatoria dentro de listas y finalmente la función devuelve el valor de lo requerido.  
def pases():
    equipo = random.choice(["Argentina", "Australia"])
    if equipo == "Argentina":
        nombre, camiseta = random.choice(equipo_argentino)
    else:
        nombre, camiseta = random.choice(equipo_australiano)
    posible_pase = random.choice([0,1])
    tiempo_partido = random.choice([0,60])
    res_string = f"{equipo};{camiseta};{nombre};{posible_pase};{tiempo_partido}"
    return res_string

# Se crean dos listas con cada equipo y dentro se encuentran varias tuplas con los datos solicitados, este tipo de colección se utiliza para evitar la modificación de los mismos.
equipo_argentino = [("Agustina Gorzelany", 7),
                    ("María José Granatto", 16),
                    ("Sofía Toccalino", 11),
                    ("Luciana Aymar", 15)
                    ]

equipo_australiano = [("Katrina Powell", 10),
                    ("Madonna Blyth", 9),
                    ("Toni Cronk", 8)
                    ]

def crearArchivo():
    # Crear un nuevo archivo
    archivo_pases = open("pases.txt", "w", encoding='utf-8')        
    cont_pases = 0
    eventos = []

    # Activar la funcion para crear un evento de pase aleatorio 50.000 veces
    while cont_pases < 50000:
        evento = pases()
        eventos.append(f"{evento}\n")
        cont_pases += 1

    archivo_pases.writelines(eventos)

crearArchivo()