#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
from datetime import datetime


def meanNA(a):
    """funcion que devuelve la media de una lista, si no hay ningun valor 'NA'"""

    prom = 0
    for i in range(len(a)):     # suma los valores si son distintos a 'NA'
        if a[i] == 'NA':
            return 'NA'
        prom += a[i]
    return prom / len(a)        # saca y devuelve el promedio


def meanProm(a):
    """Devuelve el promedio de a.
    Si hay 'NA', los valores NA se completan con el promedio de ese sensor para esa ventana.
    Si todos son NA, el valor es NA"""

    cant_NA = a.count('NA')     # cuenta los elementos 'NA'
    if cant_NA == len(a):       # chquea si son todos 'NA'
        return 'NA'
    elif cant_NA != 0:              # sino, pero hay algun 'NA'
        while a.count('NA') != 0:   # saca todos los 'NA' de la lista, para poder calcular la media
            a.remove('NA')
        suma = sum(a)               # saco el promedio de los valores
        mean = suma / len(a)
        return ((mean * cant_NA) + suma) / (len(a) + cant_NA)   # devuelve el promedio reemplazando los 'NA' con
                                                                # el promedio
    else:
        return sum(a) / len(a)  # devuelve el promedio


def Mediana(a):
    """Calucula la mediana de una lista de valores a."""

    a.sort()                # ordena la lista
    if len(a) % 2 == 0:     # si la cantidad de elementos es par, devuelve la media de los valores centrales
        print('mediana_ok')
        return (int(a[int(len(a)/2)] + a[int((len(a)/2) - 1)])) / 2
    else:                   # si la cantidad de elementos es impar, devuelve el elemento central
        print('mediana_ok')
        return a[int(len(a)/2)]


def meanMed(a):
    """Devuelve el promedio de a.
    Si hay 'NA', los valores 'NA' se completaran con la mediana de ese sensor para esa ventana.
    Si todos son 'NA', el valor es 'NA'."""

    cant_NA = a.count('NA')         # cuenta los elementos 'NA'
    if cant_NA == len(a):           # chequea si son todos 'NA'
        return 'NA'
    elif cant_NA != 0:              # sino, pero hay valores 'NA'
        while a.count('NA') != 0:   # saca todos los 'NA' de la lista, para poder calcular la mediana de los
                                        # valores restantes
            a.remove('NA')
        suma = sum(a)
        mediana = Mediana(a)
        return ((mediana * cant_NA) + suma) / (len(a) + cant_NA)    # devuelve el promedio, reemplazando los 'NA'
                                                                        # por la mediana
    else:
        return sum(a) / len(a)      # devuelve el promedio


def listar(a, n):
    """funcion que arma una lista con los eneavos elementos de cada elemento de la lista de listas a y los transforma a
    tipo de datos float.
    ej:
    a = [['1','2','3'],['4','5','6'],['7','8','9']]
    listar(a,0) = [1.0, 4.0, 7.0]
    listar(a,2) = [3.0, 6.0, 9.0]"""

    lista_nueva = []
    for i in range(len(a)):
        lista_nueva.append(a[i][n])
    return lista_nueva


def float_NA(a):
    """funcion que convierte los numeros (que estan como string) a float y deja los NA como string"""

    for i in range(len(a)):
        if a[i] != 'NA':
            a[i] = float(a[i])
    return a


def listaStr(a):
    """funcion que redondea a la segunda cifra significativa los elementos float de una lista y los convierte en str."""

    for i in range(len(a)):
        if isinstance(a[i], float):
            a[i] = round(a[i], 2)
            a[i] = str(a[i])
    return a


def main(argumentos):
    arch_entrada = argumentos[0]         # asigno los argumentos a variables
    arch_salida = argumentos[1]
    tam_ventana = int(argumentos[2])

    if len(argumentos) > 3:               # metodo idicado o deefault
        metodo = argumentos[3]
    else:
        metodo = "def"

    print('I:', arch_entrada, ' O:', arch_salida, ' L:', tam_ventana, ' M:', metodo)     # Prueba para ver los
                                                                                            # parámetros que llegaron

    # Abre los archivos de entrada (en modo R:Read) y el de salida (en modo W:Write)
    with open(arch_entrada, 'r') as entrada, open(arch_salida, 'w') as salida:

        lineasDeEntrada = []   # Aquí nos vamos a guardar toda la info del archivo de entrada

        for linea in entrada:
            linea = linea.strip('\n')         # Elimina el salto de línea del final
            camposDeLinea = linea.split(',')  # Se parte la cadena de la línea entera y se genera una lista
            # Se agrega la lista de campos de la línea a la lista de líneas completa
            lineasDeEntrada.append(camposDeLinea)

        lineasDeSalida = []

        for vent_i in range(len(lineasDeEntrada) - tam_ventana + 1):    # ciclo que recorre las ventanas

            # TRATAMIENTO DEL TIEMPO

            # crea una lista de entradas con los datos de la ventana
            entrada_vent = lineasDeEntrada[vent_i:(vent_i+tam_ventana)]
            # guardo el primer tiempo de la ventana
            tiempo_i = datetime.strptime(entrada_vent[0][0], '%Y-%m-%dT%H:%M:%S')
            # guardo el ultimo tiempo de la ventana
            tiempo_f = datetime.strptime(entrada_vent[tam_ventana - 1][0], '%Y-%m-%dT%H:%M:%S')
            # saco la diferencia de tiempos
            delta = tiempo_f - tiempo_i
            # agrega a la listaDeSalidas, una lista con el delta-t de la ventana
            lineasDeSalida.append([float(delta.seconds)])

            # TRATAMIENTO DE LAS TEMPERATURAS

            # armo listas por cada sensor, del tamaño de la ventana para sacar los promedios
            for i in range(1, len(entrada_vent[0])):    # recorre el recorte de la ventana, cada iteracion contempla
                                                            # 1(un) sensor
                sensor_i = listar(entrada_vent, i)      # hago una lista con los valores del sensor en la ventana
                sensor_i = float_NA(sensor_i)           # paso los numeros a float, y los NA los deja como str

                # agrega a la lista de la ventana el promedio de temperaturas según el metodo elegido
                if metodo == 'def':
                    lineasDeSalida[vent_i].append(meanNA(sensor_i))
                elif metodo == 'prom':
                    lineasDeSalida[vent_i].append(meanProm(sensor_i))
                elif metodo == 'med':
                    lineasDeSalida[vent_i].append(meanMed(sensor_i))
                else:
                    return print("Metodo de promedio no valido. Metodos validos: def prom med")

        for i in range(len(lineasDeSalida)):    # transforma los tipos de dato a str y redondea a la segunda cifra
                                                    # significativa
            listaStr(lineasDeSalida[i])

        for lineaPorCampos in lineasDeSalida:
            print(",".join(lineaPorCampos[:]), file=salida)  # Guarda en un archivo los campos originales


# Sólo si el programa es ejecutado (esto es, no se usa con 'import') se ejecturará lo de abajo
if __name__ == "__main__":

    if len(sys.argv) < 4:
        print("Se esperaban más argumentos:\n taller3.py arch_entrada arch_salida tam_ventana [metodo_na]")
        sys.exit(1)

    main(sys.argv[1:])
