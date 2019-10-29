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


def suma_3(a, b, c):
    """devuelve la suma de tres (3) numeros reales (a, b, y c)"""

    x = a + b + c
    return x


def promedio_3(a, b, c):
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


def menor_2(a, b):
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
            if n % i == 0:
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


def primo(n):
    """devuelve True si n es primo"""

    if sumaDivisores(n) == n + 1:
        return True
    return False


def menorDivisiblePorTres(n):
    """dado un n positivo, devuelve el menor numero mayor a n tal que sea divisible por 3"""

    res = n + 1
    while res % 3 != 0:
        res += 1
    return res


def mayorPrimo(n1, n2):
    """devuelve True si n1 es el mayor primo que divide a n2"""

    divisores_n2 = divisores(n2)
    print(divisores_n2)
    i = -1
    while primo(divisores_n2[i]) == False:
        i -= 1
    if divisores_n2[i] == n1:
        return True
    return False


def potencia(n1, n2):
    """devuelve True si n1 es una potencia de n2"""

    i = 1
    while n2 ** i < n1:
        i += 1
    if n2 ** i == n1:
        return True
    return False


def mcd(n1, n2):
    """devuelve el maximo comun divisor entre n1 y n2"""

    div_n1 = divisores(n1)
    div_n2 = divisores(n2)
    div_comunes = []
    for i in range(len(div_n1)):
        if div_n1[i] in div_n2:
            div_comunes.append(div_n1[i])
    return div_comunes[-1]


##----------EJERCICIO 4----------
##-------------------------------


def suma(a):
    """devuelve la suma de todos los elementos de la lista a"""

    suma = 0
    for i in range(len(a)):
        suma += a[i]
    return suma


def promedio(a):
    """devuelve el promedio de los elementos de la lista a"""

    if len(a) > 0:
        return suma(a) / len(a)
    else:
        return 'lista sin valores'


def maximo(a):
    """devuelve el maximo entre todos los elementos de una lista a"""

    ordenar(a)
    return a[-1]


def listaDeAbs(a):
    """devuelve una lista con los valores absolutos de cada elemento de la lista a"""

    for i  in range(len(a)):
        a[i] = abs(a[i])
    return a

def maximoAbsoluto(a):
    """devuelve el maximo entre los valores absolutos de todos los elementos de la lista a"""

    a = listaDeAbs(a)
    a = ordenar(a)
    return a[-1]


## def divisores(n) --->> esta resuelto en el ejercicio2


def cantidadApariciones(a, x):
    """devuelve la cantidad de veces que se repite el elemento x en la lista a"""

    cant = 0
    for i in range(len(a)):
        if a[i] == x:
            cant += 1
    return cant


def masRepetido(a):
    """devuelve el elemento que mas veces aparece en la lista a"""

    masRep = cantidadApariciones(a[0])
    for i in range(1, len(a)):
        if cantidadApariciones(a, a[i]) > masRep:
            masRep = a[i]
    return masRep


def todosPares(a):
    """devuelve True si todos los elementos de la lista a son pares"""

    for i in range(len(a)):
        if par(a[i]) == False:
            return False
    return True


### def ordenAscendente(a)  ---->>> en el Taller2 hay una igual


def reverso(a):
    """devuelve una lista que cumple que sus elementos son los mismos que los de a, pero en orden inverso"""

    inverso = []
    for i in range(len(a)):
        inverso.insert(-len(inverso), a[i])
    return inverso


# ----------EJERCICIO 5----------
# -------------------------------

# a
def raiz(n):
    """saca la raiz cuadrada"""
    return n ** (1/2)

#b
def suma_indices_pares(a):
    """suma los elementos con indice par de una lista a"""

    suma_i = 0
    for i in range(len(a)):
        if i % 2 == 0:
            suma_i += a[i]
    return suma_i


def es_espejo(a):
    """devuelve True si los elementos de una lista se repiten desde el/los elementos centrales"""

    medio = int(len(a) / 2)
    if len(a) % 2 == 1:
        for i in range(medio):
            if a[i] != a[len(a) - 1 - i]:
                return False
    else:
        for i in range(medio - 1):
            if a[i] != a[len(a) - 1 - i]:
                return False
    return True


def prom_elem_indice_impar(a):
    """devuelve el promedio de los elementos de indice par de a. Siempre que a no sea vacia"""

    if a = []:
        print('error de entrada. lista vacia')
    suma_i = 0
    for i in range(len(a)):
        if i % 2 == 1:
            suma_i += a[i]
    return suma_i / (len(a) / 2)

def menor(a):
    """devuelve el elemento con valor minimo de una lista a"""

    ordenar(a)
    return a[0]
