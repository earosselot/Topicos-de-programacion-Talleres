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
    if len(a) == 0:
        return None
    else:
        a[0] = abs(a[0])
    return lista_de_abs(a[1:])
