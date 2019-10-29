# EJERCICIO 1 #

def fact(n):
    if n == 1:
        return 1
    else:
        return n * fact(n - 1)


def fib(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib(n - 1) + fib(n - 2)


def sumPot2(a, b):
    if a - b == 0:
        return 2 ** b
    else:
        return 2 ** b + sumPot2(a, b - 1)


def impar(n):
    if n % 2 == 0:
        return False
    else:
        return True


def sumImp(n):
    if 0 < n <= 3:
        return 1
    elif impar(n) == False:
        return n - 1 + sumImp(n - 2)
    elif impar(n) == True:
        return n - 2 + sumImp(n - 2)


def sumaDigitos(n):
    if n < 100:
        return n % 10 + n // 10
    else:
        return n % 10 + sumaDigitos(n // 10)


def divisores(n, div, a):
    if n % div == 0:
        a.append(div)
    if div == 1:
        return None
    divisores(n, div-1, a)

def suma_lista(a):
    if len(a) == 0:
        return 0
    else:
        return a[0] + suma_lista(a[1:])


def suma_div(n):
    divis = []
    divisores(n, n, divis)
    print(divis)
    return suma_lista(divis)


def divisible_por_3(n):

    div3 = [3, 6, 9]
    no_div3 = [1, 2, 4, 5, 7, 8]
    if n in div3:
        return True
    elif n in no_div3:
        return False
    else:
        return divisible_por_3(sumaDigitos(n))


def divX17(n):
    if n == 17 or n == 0:
        return True
    elif n < 17:
        return False
    elif n > 17:
        a = (n % 10) * 5
        b = (n // 10) - a
        b = (b ** 2) ** (1 / 2)
        return divX17(b)


# EJERCICIO 2

# def suma(a): ESTA ARRIBA COMO suma_lista(a)

def suma(a):
    if len(a) == 0:
        return 0
    else:
        return a[0] + suma(a[1:])


def maximo(a):
    if len(a) == 1:
        return a[0]
    elif a[0] > a[1]:
        a.pop(1)
        return maximo(a)
    else:
        a.pop(0)
        return maximo(a)


def promedio(a):
    return suma(a) / len(a)


def lista_de_abs(a):
    if len(a) == 1:
        return [abs(a[0])]
    else:
        return [abs(a[0])] + lista_de_abs(a[1:])

def maximoAbsoluto(a):
    return maximo(lista_de_abs(a))


def cambio_de_base(n, x):
    if n // x == 1 or n // x == 0:
        return [n // x, n % x]
    else:
        return cambio_de_base(n // x, x) + [n % x]


def cantidad_apariciones(a, x):
    if len(a) == 0:
        return 0
    elif a[0] == x:
        return 1 + cantidad_apariciones(a[1:], x)
    else:
        return cantidad_apariciones(a[1:], x)

def eliminar(a, x):
    if x == 0:
        return a[1:]
    else:
        return [a[0]] + eliminar(a[1:], x-1)

def seekANDdestroy(a, x):
    if len(a) == 1:
        if a[0] == x:
            return []
        else:
            return [a[0]]
    elif a[0] == x:
        return seekANDdestroy(a[1:], x)
    else:
        return [a[0]] + seekANDdestroy(a[1:], x)


def todos_pares(a):
    if len(a) == 1:
        if a[0] % 2 == 0:
            return True
        else:
            return False
    elif a[0] % 2 == 0:
        return True and todos_pares(a[1:])
    else:
        return False

def ordenAscendente(a):
    if len(a) == 2:
        if a[0] <= a[1]:
            return True
        else:
            return False
    elif a[0] <= a[1]:
        return True and ordenAscendente(a[1:])
    else:
        return False

def reverso(a):
    if len(a) == 1:
        return [a[0]]
    else:
        return reverso(a[1:]) + [a[0]]


def sumaPosImpares(a):

    if len(a) < 1:
        return 0
    elif len(a) == 2 or len(a) == 3:
        return a[1]
    else:
        return a[1] + sumaPosImpares(a[2:])


def max_i(a):
    """devuelve el indice del maximo de a"""

    if len(a) < 1:
        if a[0] > a[1]:
            return
    if a[0] >= a[1]:
        return

def triangular(a):


    max = maximo(a)
    if len(a) == 1:
        return True


