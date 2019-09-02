# Topicos de programacion 2019 - Eduardo Rosselot
# Taller 0

import random as rnd

# Funcion que genera un mazo a partir de sumar n mazos de 52 cartas. n es la cantidad de jugadores
def generarMazo(n):
    # armo un_mazo de 52 cartas con 4 cartas de cada numero entre 1 y 13
    m = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
    # m = [1, 2, 3]
    un_mazo = m + m + m + m

    # creo el_mazo y suma un mazo por cada jugador
    el_mazo = []
    for i in range(n):
        el_mazo += un_mazo

    # mezcla el_mazo
    rnd.shuffle(el_mazo)

    # devuelve el_mazo
    return el_mazo


# Funcion que toma cartas del mazo hasta llegar a un numero mayor igual a 21 y devuelve la suma.
def jugar(m):
    # inicializo el puntaje, si no quedan cartas en el mazo, queda en cero.
    suma_jugador = 0

    # toma cartas y suma al total hasta que la suma sea mayor igual a 21.
    while suma_jugador < 21:

        # si hay cartas en el mazo, roba una.
        if len(m) > 0:
            suma_jugador += m.pop(0)
        # Si no hay, sale del bucle y queda con el puntaje que tenia (si robó alguna carta), o en 0 (si no alcanzó a
        # robar)
        else:
            break

    # devuelve el resultado de la jugada
    return suma_jugador


# Funcion que hace jugar a varios jugadores y devuelve una lista con los resultados de cada uno.
def jugar_varios(m, j):
    juego = []
    for i in range(j):
        juego.append(jugar(m))
    return juego


# Funcion que toma cartas del mazo hasta llegar a un numero mayor igual a 19 y devuelve la suma.
def jugarMiedo(m):
    # inicializo el puntaje, si no quedan cartas en el mazo, queda en cero.
    suma_jugador = 0

    # toma cartas y suma al total hasta que la suma sea mayor igual a 19.
    while suma_jugador < 19:

        # si hay cartas en el mazo, roba una.
        if len(m) > 0:
            suma_jugador += m.pop(0)
        # Si no hay, sale del bucle y queda con el puntaje que tenia (si robó alguna carta), o en 0 (si no alcanzó a
        # robar)
        else:
            break

    # devuelve el resultado de la jugada
    return suma_jugador


# Funcion que toma cartas del mazo de manera aleatoria o hasta que sea mayor igual a 21 y devuelve la suma.
def jugarBorracho(m):
    # asigno 0 a la suma del juego y 1 a la moneda (de manera que sea mayor a 0,5 y tome la primer carta)
    suma_jugador = 0
    moneda = 1

    # toma cartas y suma al total hasta que la suma sea mayor igual a 21 o hasta que la moneda genere un numero menor
    # a 0,5.
    while suma_jugador < 21 and moneda > 0.5:

        # si hay cartas en el mazo, roba una.
        if len(m) > 0:
            suma_jugador += m.pop(0)
        # Si no hay, sale del bucle y queda con el puntaje que tenia (si robó alguna carta), o en 0 (si no alcanzó a
        # robar)
        else:
            break

        moneda = rnd.random()

    # devuelve el resultado de la jugada
    return suma_jugador


def jugarSmart(m):
    # asigno 0 a la suma del juego, 1 a la moneda y -1 al smart (de manera que tome la primer carta)
    suma_jugador = 0
    smart = -1
    azar = 1

    # toma cartas dependiendo de la cercanía a 21 (si tiene 21 no toma, porque smart se hace igual a 1 y el numero
    # random no puede ser mayor a 1)
    while azar > smart:

        # si hay cartas en el mazo, roba una.
        if len(m) > 0:
            suma_jugador += m.pop(0)
        # Si no hay, sale del bucle y queda con el puntaje que tenia (si robó alguna carta), o en 0 (si no alcanzó a
        # robar)
        else:
            break

        # genera un numero random entre 0 y 1
        azar = rnd.random()

        # funcion lineal que pasa por (8,0) y (1,21) y genera el numero para comparar con el aleatorio:
        # 1) Para suma_jugador < 8, smart < 0 => azar > smart => entra al loop
        # 2) Para suma_jugador = 21, smart = 1 => azar > smart nunca se cumple => no vuelve a entrar al loop si
        # tiene 21 o mas.
        # 3) Para valores de suma_jugador entre 9 y 20 smart toma valores crecientes entre 0 y 1 con distrubición lineal,
        # al aumentar el valor de suma_jugador smart crece y es menos probable que se cumpla la condición azar > smart,
        # es decir, es menos probable que robe un carta.
        smart = (suma_jugador / 13) - 8 / 13

    # devuelve el resultado de la jugada
    return suma_jugador


# Funcion que permite compara los resultados de distintas estrategias de juego
def compararEstrategia(lista_jug, m):

    # genero una lista vacia para almacenar los resultados
    resultados = []

    # loop que recorre la lista de jugadores de entrada (lista_jug)
    for i in range(len(lista_jug)):

        # secuencia de if's que juega con distintas estrategias dependiendo de los valores de entrada, y va anexando los
        # resultados a una lista
        if lista_jug[i] == 0:
            resultados.append(jugar(m))
        if lista_jug[i] == 1:
            resultados.append(jugarMiedo(m))
        if lista_jug[i] == 2:
            resultados.append(jugarBorracho(m))
        if lista_jug[i] == 3:
            resultados.append(jugarSmart(m))

    return resultados

# Armo la lista de jugadores
lista_jugadores = [0, 2, 1, 3, 0, 1, 2, 3, 3, 3, 3, 4]

# Armo el mazo
mazo = generarMazo(len(lista_jugadores))

# Se juega y se imprime lo que resta del mazo y los resultados de cada jugador
while len(mazo) > 1:
    res = compararEstrategia(lista_jugadores, mazo)
    print('resultados: ', res)
    if len(mazo) != 0:
        print('mazo restante: ', mazo)
    else:
        print('no hay mas cartas - fin del juego')