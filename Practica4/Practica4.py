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

def sumaDivisores(n):



def sumaDigitos(n):
    if n < 100:
        return n % 10 + n // 10
    else:
        return n % 10 + sumaDigitos(n // 10)


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