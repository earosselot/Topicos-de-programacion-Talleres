#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
from datetime import datetime

def meanNA(a):
    prom = 0
    for i in range(len(a)):
        if a[i] == 'NA':
            return 'NA'
        prom += a[i]

    prom = prom / len(a)
    return prom

def meanProm(a):
    """Los valoresNA se completan con el promedio de ese sensor para esa ventana. Sitodos son NA, el valor es NA"""
    suma = 0
    cantidad_num = 0
    cantidad_NA = 0

    for i in range(len(a)):
        if a[i] != 'NA':
            suma += a[i]
            cantidad_num += 1
        else:
            cantidad_NA += 1

    if cantidad_num == 0:
        return 'NA'
    elif cantidad_NA != 0:
        while a.count('NA') != 0:
            a.remove('NA')
        mean = suma / cantidad_num
        Prom = ((mean * cantidad_NA) + suma) / (len(a))
        return Prom
    else:
        return suma / len(a)

def Mediana(a):

    a.sort()
    if len(a) % 2 == 0:
        print('mediana_ok')
        return ( int(a[int(len(a)/2)] + a[int((len(a)/2) - 1)]) ) / 2
    else:
        print('mediana_ok')
        return a[int(len(a)/2)]

def meanMed(a):

    suma = 0
    cantidad_num = 0
    cantidad_NA = 0

    for i in range(len(a)):
        if a[i] != 'NA':
            suma += a[i]
            cantidad_num += 1
        else:
            cantidad_NA += 1

    if cantidad_num == 0:
        return 'NA'
    elif cantidad_NA != 0:
        while a.count('NA') != 0:
            a.remove('NA')
        mediana = Mediana(a)
        return ((mediana * cantidad_NA) + suma) / (len(a))
    else:
        return suma / len(a)

def meanDist(a):
    return a

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

    for i in range(len(a)):
        tipo = type(a[i])
        print(tipo)
        if isinstance(a[i], float) or isinstance(a[i], int):
            print('asd')
            a[i] = round(a[i], 2)
            a[i] = str(a[i])
    return a

def main(argumentos):
    arch_entrada = argumentos [ 0 ]
    arch_salida = argumentos [ 1 ]
    tam_ventana = int(argumentos [ 2 ])

    if len( argumentos ) > 3:
        metodo = argumentos [ 3 ]
    else:
        metodo = "def"

    print('I:',arch_entrada, ' O:', arch_salida, ' L:', tam_ventana, ' M:', metodo) # Prueba para ver los parámetros que llegaron

    with open( arch_entrada, 'r' ) as entrada, open( arch_salida,
                                                     'w' ) as salida:  # Abre los archivos de entrada (en modo R:Read) y el de salida (en modo W:Write)
        lineasDeEntrada = [ ]  # Aquí nos vamos a guardar toda la info del archivo de entrada

        print(entrada)
        for linea in entrada:
            linea = linea.strip( '\n' )  # Elimina el salto de línea del final
            camposDeLinea = linea.split( ',' )  # Se parte la cadena de la línea entera y se genera una lista
            lineasDeEntrada.append(
                camposDeLinea )  # Se agrega la lista de campos de la línea a la lista de líneas completa

        print(lineasDeEntrada)  # Prueba para ver que se haya leído bien el archivo de entrada

        lineasDeSalida = []

        for vent_i in range(len(lineasDeEntrada) - tam_ventana + 1):    # ciclo que recorre las ventanas

            # TRATAMIENTO DEL TIEMPO
            entrada_vent = lineasDeEntrada[vent_i:(vent_i+tam_ventana)]     # crea una lista de entradas con los datos de la ventana
            tiempo_i = datetime.strptime(entrada_vent[0][0], '%Y-%m-%dT%H:%M:%S')   # guardo el primer tiempo de la ventana
            tiempo_f = datetime.strptime(entrada_vent[tam_ventana - 1][0], '%Y-%m-%dT%H:%M:%S')     # guardo el ultimo tiempo de la ventana
            delta = tiempo_f - tiempo_i     # saco la diferencia de tiempos
            lineasDeSalida.append([delta.seconds])

            # armo listas por cada sensor, del tamaño de la ventana para sacar los promedios
            for i in range(1, len(entrada_vent[0])):    # recorre el recorte de la ventana
                sensor_i = listar(entrada_vent, i)
                sensor_i = float_NA(sensor_i)
                if metodo == 'def':
                    lineasDeSalida[vent_i].append(meanNA(sensor_i))
                elif metodo == 'prom':
                    lineasDeSalida[vent_i].append(meanProm(sensor_i))
                elif metodo == 'med':
                    print("entre aca")
                    lineasDeSalida[vent_i].append(meanMed(sensor_i))
                elif metodo == 'dist':
                    lineasDeSalida[vent_i].append(meanDist(sensor_i))

        for i in range(len(lineasDeSalida)):
            listaStr(lineasDeSalida[i])

        print('salida_str:', lineasDeSalida)

        for lineaPorCampos in lineasDeSalida:
            print( ",".join( lineaPorCampos [ 1: ] ),
                   file=salida )  # Guarda en un archivo los campos originales, sin la primera columna

# Sólo si el programa es ejecutado (esto es, no se usa con 'import') se ejecturará lo de abajo

if __name__ == "__main__":

    if len( sys.argv ) < 4:
        print( "Se esperaban más argumentos:\n taller3.py arch_entrada arch_salida tam_ventana [metodo_na]" )
        sys.exit( 1 )

    main( sys.argv [ 1: ] )


