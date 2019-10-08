#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
from datetime import datetime

def meanNA(a):

    prom = 0
    for i in range(len(a)):
        if a[i] == "NA":
            return "NA"
        prom += a[i]

    prom = prom / len(a)

    return prom

def main1(argumentos):
    arch_entrada = argumentos [ 0 ]
    arch_salida = argumentos [ 1 ]
    tam_ventana = argumentos [ 2 ]

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

        print(lineasDeEntrada) # Prueba para ver que se haya leído bien el archivo de entrada

        # Con los datos cargados, ya se puede hacer el procesamiento#
        lineasDeSalida = lineasDeEntrada  # Sólo se copia la entrada, a efectos de probar la salida

        # METODO DEFAULT
        if metodo == "def":
            # Si alguno de los valores dentro de esta ´ultima fuera NA, el promedio debe dar NA
            print("metodo default")
            print(len(lineasDeEntrada[1]))
            promedios = []
            for vent in range(len(lineasDeEntrada)- tam_ventana):
                for i in range(tam_ventana):
                    promedios.insert(,"PROMEDIO DEL TIMEPO")
                    for j in range(1, len(lineasDeEntrada[1])):
                        promedios.insert([i][j], "PROMEDIO DE LAS TEMPERATURAS")
            print("salida :", promedios)



        # METODO PROMEDIO
        elif metodo == "prom":
            # Los valores NA se completar´an con el promedio de ese sensor para esa ventana. Si
            # todos son NA, el valor es NA
            print("metodo prom")

        # METODO MEDIANA
        elif metodo == "med":
            # Los valores NA se completar´an con la mediana de ese sensor para esa ventana. Si
            # todos son NA, el valor es NA
            print( "metodo med" )


        # METODO DISTRIBUCION
        elif metodo == "dist":
            # Valores de la misma distribuci´on de valores. As´ı, se debe genera nuevos valores a
            # partir de la distribuci´on de todos los valores de esa ventana. Probar qu´e ocurre si se toman
            # todos los valores (la lista completa).
            print( "metodo dist" )

        else:
            print("Metodo no válido")


        for lineaPorCampos in lineasDeSalida:
            print( ",".join( lineaPorCampos [ 1: ] ),
                   file=salida )  # Guarda en un archivo los campos originales, sin la primera columna

# Sólo si el programa es ejecutado (esto es, no se usa con 'import') se ejecturará lo de abajo

entrada = "entrada1.csv"
salida = "salida.csv"
ventana = 3
metodo = "def"

argumentos = [entrada, salida, ventana, metodo]

main1(argumentos)

a = [1, 5, 8, "NA"]
print(meanNA(a))

# if __name__ == "__main__":
#
#     if len( sys.argv ) < 4:
#         print( "Se esperaban más argumentos:\n taller3.py arch_entrada arch_salida tam_ventana [metodo_na]" )
#         sys.exit( 1 )
#
#     main( sys.argv [ 1: ] )


