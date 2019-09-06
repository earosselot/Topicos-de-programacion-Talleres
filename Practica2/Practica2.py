##----------EJERCICIO 1----------
##-------------------------------

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

    x = (n * n) ** (1 / 2)
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
    """devuelve una lista ordenada de menor a mayor de numeros reales [lista], a partir de una ordenada o no ordenada"""

    i = 0
    while i < len(lista) - 1:
        while i < len(lista) - 1 and lista[i] < lista[i + 1]:
            i = i + 1
        if i < 2:
            mayor = lista[i]
            menor = lista[i + 1]
            lista[i] = menor
            lista[i + 1] = mayor
            i = 0
    return lista


def maximo3(a, b, c):
    """devuelve el maximo entre 3 numeros reales (a, b y c)"""

    lista = [a, b, c]
    x = ordenar(lista)
    return x[2]


def maxAbs(a, b, c):
    """devuelve el valor absoluto maximo entre 3 numeros (a, b y c)"""

    lista = [abs(a), abs(b), abs(c)]
    x = maximo3(lista[0], lista[1], lista[2])
    return x


##----------EJERCICIO 2----------
##-------------------------------


def noEsCero(n):
    """Funcion que devuelve True si un numero(n) no es == 0"""

    if n != 0:
        x = True
    else:
        x = False
    return x


def iguales(a, b):
    """Funcion que devuelvo True si dos numeros (a y b) son iguales"""

    if a == b:
        x = True
    else:
        x = False
    return x


def menor(a, b):
    """Funcion que devuelve True si a es menor que b"""

    if a < b:
        x = True
    else:
        x = False
    return x


def par(n):
    """funcion que devuelve True si un numero (n) es par"""

    if n % 2 == 0:
        x = True
    else:
        x = False
    return x


def divisible(n, d):
    """funcion que devuelve True si un numero(n) es divisible por otro(d)
    d no puede ser 0"""

    if n % d == 0:
        x = True
    else:
        x = False
    return x


def imparDivisiblePorTresOCinco(n):
    """Funcion que devuelve True si un numero (n) es divisible por 3 o 5, pero no por 2"""

    if ((n % 3 == 0) or (n % 5 == 0)) and (n % 2 != 0):
        x = True
    else:
        x = False
    return x


##----------EJERCICIO 3----------
##-------------------------------

def factorial(n):
    """Funcion que devuelve el factorial de un numero (n)"""

    if n == 0:
        fact = 1
    elif n > 0:
        fact = n
        while n > 1:
            n = n - 1
            fact = fact * n
    return fact


def divisores(n):
    """funcion que devuelve una lista con los divisores de un numero (n)"""

    if n != 0:
        n = int(abs(n))
        listaDivisores = []
        for i in range(1, n + 1):
            if divisible(n, i):
                listaDivisores.append(i)
    else:
        listaDivisores = 'infinitos'
    return listaDivisores


def sumaLista(lista):
    """funcion que suma todos los valores de una lista"""

    suma = 0
    for i in range(len(lista)):
        suma += lista[i]
    return suma


def sumaDivisores(n):
    """funcion que devuelve la suma de los divisores de un numero (n)"""

    listaDivisores = divisores(n)
    x = sumaLista(listaDivisores)
    return x
