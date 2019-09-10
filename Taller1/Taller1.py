## ---------------------------------------------- EJERCICIO 1 ----------------------------------------------

def QueFieston(a):
    # La funcion recibe un lista de numeros en principio, por eso compara
    chuki = 200
    i= 0
    robi = 0
    ## d = 0 ## esto no se usa para nada
    while i < len(a):
        # este while va a recorrer toda la lista de entrada (a).
        # Cuenta la cantidad de veces que se repite (robi) el menor de los numeros(chuki) entre 0 y 200

        if a[i] == chuki: #si alguno de los valores de la lista es 200 (==chuki) le sumo 1 a robi
            robi += 1
        elif a[i] < chuki and a[i] > 0:
            # si el valor de la lista es mayor a 0 y menor a chuki... cambia el valor a chuki por el de la lista y robi vuelve a 1
            robi = 1
            chuki = a[i]
        i += 1
    chimbote = robi * chuki
    # multiplica el menor numero por la cantidad de veces que se repite
    print(chimbote, robi, chuki)
    return chimbote


## ---------------------------------------------- EJERCICIO 2 ----------------------------------------------


def esPrimo(x):
    """funcion que devuelve True si x es un numero primo"""

    i = 2
    res = True
    while i <= (x ** (1/2)) and res != False:
        if x % i == 0:
            res = False
        i += 1
    return res
    # div = 0                     # inicializacion del contador de divisores en 0
    # for i in range(1, x+1):     # recorre todos los numeros enteros entre 1 y x
    #     if x % i == 0:          # suma al contador de divisores si el resto de la division da 0
    #         div += 1
    # if div == 2:                # si solo tiene 2 divisores, entonces es un numero primo y asigna True a res
    #     res = True
    # else:
    #     res = False             # en cualquier otro caso asigna False a la variable res
    # return res


def es2N1(x):
    """funcion que devuelve True si x es un numero anterior a una potencia de 2"""

    n = 1                       #inicializo las variables n y el resultado, que por omisión es Falso
    res = False
    while (2 ** n) - 1 <= x:    # Hago la cuenta aumentando el valor de n (la potencia)
                                # mientras los resultados sean menores iguales al numero x
        if (2 ** n) - 1 == x:   # Si el numero se puede expresar como (2**n)-1 res pasa a ser True
            res = True
        n += 1
    return res


def Resacon(n):
    """función que se encontró entre botas de contenido incierto y ropa interior de recorrido y estado dudoso
    Además de eso, devuelve el eneavo numero primo y que es anterior a una potencia de 2"""

    numero = 2                                  # inicializo la variable numero desde 2 (por definicion de numeros primos)
    contador = 0                                # inicializo en contador en 0
    while contador < n:                         # este ciclo chequea los enteros desde el 2 hasta que n numeros cmplan
                                                # con las condiciones (es2N1 y esPrimo)
        if es2N1(numero) and esPrimo(numero):   # cuando un numero cumple la condicion aumenta el contador en uno y guarda
                                                # ese numero en res. En caso de que sea el eneavo, es el valor que va a devolver
            res = numero
            contador += 1
            print(contador, res)
        numero += 1
    return res


Resacon(8)