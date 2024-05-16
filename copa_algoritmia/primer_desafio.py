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

        visto = nombre in jugadores_visto
        if not visto:
            jugadores_visto.append(nombre)

            jugador_dict = {
            'numero': camiseta,
            'nombre': nombre, 
            'cantidad_pases': 1,
            'pases_bien': 1 if posible_pase == '1' else 0, 
            'pases_mal': 1 if posible_pase == '0' else 0, 
            'porcentaje': 100.00 if posible_pase == '1' else 0.00
            }
        
            if equipo == 'Australia':
                australia_pases.append(jugador_dict)
            elif equipo == 'Argentina':
                argentina_pases.append(jugador_dict)





    australia = {'Australia': australia_pases}
    argentina = {'Argentina': argentina_pases}

    print(jugadores_visto)
    
    print([australia, argentina])

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

# Ejecutar programa
if __name__ == "__main__":
    crearArchivo()

# [{'Australia': [{'numero': '10', 'nombre': 'Katrina P', 'cantidad_pases': 454,
# 'pases_bien': 243, 'pases_mal': 211, 'porcentaje': 53.15}, {}]}, 
# {'Argentina': []}]