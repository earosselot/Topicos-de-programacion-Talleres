def Saltos(a, h):
    """funcion de devuelve una lista (saltos) con las posiciones de los saltos de altura h de una lista a"""

    saltos = []                         # inicializo la lista de posiciones de saltos vacía

    for i in range(len(a) - 1):         # recorro la lista hasta el penultimo valor
        if h == abs(a[i + 1] - a[i]):   # si la diferencia entre un elemento y el siguiente es igual a h,
            saltos.append(i)            # agrego el valor de la posicion del salto a la lista saltos

    return saltos                       # devuelvo la lista de posiciones


def hayBorde(a, n, h):
    """funcion que recibe como paramentros una lista (a), un tamaño (n) y una altura de salto (h). Devuelve True si la
    lista a tiene al menos un salto de tamaño n y altura h"""

    saltos = Saltos(a, h)   # busco las ubicaciones de los saltos de altura h
    if saltos == []:        # si no hay saltos de altura h, no miro el tamaño y devuelve False
        return False

    # elimino de la lista de posiciones de saltos las posiciones que no van con el largo de la lista a. Ej.: si el salto
    # esta en la posicion 3, y el parametro n es 5, no pueden haber antes del salto 5 numero iguales, entonces descarto
    # esa poscion de salto. Lo mismo si estuvira cerca del final de la lista.
    # con las posiciones de los saltos que pueden cumplir la condicion de tamaño, armo la lista saltos_ok
    saltos_ok = []
    for g in range(len(saltos)):                    # recorre la lista de saltos
        if n - 1 <= saltos[g] <= (len(a) - n - 1):  # si cumple con la condicion, lo agrego a la lista de saltos_ok
            saltos_ok.append(saltos[g])

    for k in range(len(saltos_ok)):                     # recorro la lista de posiciones de saltos
        m = 1                                           # inicializo m, para probar el tamaño del salto a izquierda y
                                                        # a derecha
        j = saltos_ok[k]                                # asigno a j el valor de la posicion del salto k

        # me fijo que los n valores de los elementos anteriores y posteriores, uno por uno (con m), al salto sean iguales,
        while m < n and a[j] - a[j - m] == 0 and a[j + 1] - a[j + 1 + m] == 0:
            if m == n - 1:              # si llega al tamaño requerido, devuelve true
                return True
            m += 1

    # devuelve False si habia saltos de la altura requerida, pero no del tamaño requerido
    return False

def EsCreciente(a):
    """funcion que devuelve True si una lista (a) es creciente, o vacía"""

    if a == []:                 # devuelve True si la lista es vacía
        return True

    for i in range(len(a)-1):   # recorre la lista elemento por elemento
        if a[i] > a[i+1]:       # si algun valor es mayor al siguente (no es creciente), devuelve False y termina
            return False
    return True                 # si completa el ciclo for, nunca un valor es mayor al seguiente (es creciente), devuelve True

def EsDecreciente(a):
    """funcion que devuelve True si una lista (a) es decreciente, o vacía"""

    if a == []:                 # devuelve True si la lista es vacía
        return True

    for i in range(len(a)-1):   # recorre la lista elemento por elemento
        if a[i] < a[i+1]:       #  si algun valor es menor al siguente (no es decreciente), devuelve False y termina
            return False
    return True                 # si completa el ciclo for, nunca un valor es menor al seguiente (es decreciente), devuelve True

def maxPos(a):
    """funcion que devuelve la posicion del valor máximo de un lista(a)"""

    max = a[0]                  # asigno como valor maximo al primer valor
    max_pos = 0                 # asigno como posicion del valor maximo la primera posicion
    for i in range(len(a)):     # recorro la lista (a)
        if a[i] > max:          # si hay un valor mayor al maximo actual, actualiza el valor del maximo y la posicion
            max = a[i]
            max_pos = i
    return max_pos              # devuelve la posicion del valor máximo

def listaTriangular(a):
    """funcion que devuelve True si la lista es triangular"""

    if a == []:                     # por definicion la lista vacia es triangular
        return True

    max_pos = maxPos(a)             # ecuentro el valor maximo de la lista
    termino1 = a[0: max_pos]        # divido la lista en dos terminos, hasta y desde el maximo
    termino2 = a[max_pos:]
    if EsCreciente(termino1) == True and EsDecreciente(termino2) == True:   # si se cumple que la lista es creciente
                                                                            # hasta el maximo y decreciende desde el
                                                                            # maximo, devuelve True
        return True
    return False                                                            # sino, devuelve False

a = [1, 3, 4, 5]
b = []
c = [1, 2, 3, 5, 4, 2, 1]
print(maxPos(a))
print(listaTriangular(a))
print(listaTriangular(b))
print(listaTriangular(c))


a = [1, 1, 1, 3, 3, 3, 4, 5, 8, 8, 8, 11, 11, 15, 21, 21, 30, 15, 15, 15, 4, 4, 4]
# a = [1, 2, 4, 5]
saltos = Saltos(a, 2)
print(saltos)
print('len(a)', len(a))
print(hayBorde(a, 3, 3))

