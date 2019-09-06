import math

def doble(n):
    """funcion que devuelve el doble de un numero real"""

    x = n * 2
    return x


def signo(n):
    """"funcion que devuelve el signo de un numero real (n), si la entrada es 0, devuelve 0"""

    if n < 0:
        x = -1
    elif n == 0:
        x = 0
    else:
        x = 1
    return x


def abs(n):
    """funcion que devuelve el valor absoluto de un numero real (n)"""

    x = math.sqrt(n * n)
    return x


def invMult(n):
    """funcion que devuelve el inverso multiplicativo de un numero real (n), distinto de 0"""

    x = 0
    if n != 0:
        x = 1 / n
    return x


def suma(a, b, c):
    """devuelve la suma de tres (3) numeros reales (a, b, y c)"""

    x = a + b + c
    return x


def promedio(a, b, c):
    """devuelve el promedio de tres numeros reales (a, b y c)"""

    x = suma(a, b, c) / 3
    return x


def ordenar(lista):
    """devuelve una lista ordenada de numeros reales [lista], a partir de una ordenada o no ordenada"""

    i = 0
    while i < len(lista) - 1:
        while i < len(lista) - 1 and lista[i] < lista[i+1]:
            i = i + 1
        if i < 2:
            mayor = lista[i]
            menor = lista[i+1]
            lista[i] = menor
            lista[i+1] = mayor
            i = 0
    return lista


def maximo3(a, b, c):
    """devuelve el maximo entre 3 numeros reales (a, b y c)"""

    lista = [a, b, c]
    x = ordenar(lista)
    return x[2]