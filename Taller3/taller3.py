#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
from datetime import datetime

def main(argumentos):
    arch_entrada = argumentos[0]
    arch_salida  = argumentos[1]
    tam_ventana  = argumentos[2]
     
    if len(argumentos)> 3:
        metodo = argumentos[3]
    else:
        metodo = "INDEFINIDO"
    
    # print('I:',arch_entrada, ' O:', arch_salida, ' L:', tam_ventana, ' M:', metodo) # Para ver los parámetros que llegaron
    
    with open(arch_entrada, 'r') as entrada, open(arch_salida, 'w') as salida:
        for linea in entrada:
        
            linea = linea.strip('\n')         # Elimina el salto de línea
            lineaPorCampos = linea.split(',') # Parte la cadena en una lista, en las comas
            
            # PROCESAMIENTO DE LOS DATOS #
            
            print(",".join(lineaPorCampos[1:]), file=salida) # Guarda en un archivo los campos originales, sin la primera columna


# Sólo si el programa es ejecutado (esto es, no se usa con 'import') se ejecturará lo de abajo
if __name__ == "__main__":

    if len(sys.argv) < 4:
        print("Se esperaban más argumentos:\n taller3.py arch_entrada arch_salida tam_ventana [metodo_na]")
        sys.exit(1)
    
    main(sys.argv[1:])

