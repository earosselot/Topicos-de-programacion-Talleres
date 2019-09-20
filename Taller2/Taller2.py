def Saltos(a, h):
    saltos = []
    # i = 0
    for i in range(len(a) - 1):
        if abs(a[i + 1] - a[i]) >= h:
            saltos.append(i)

    return saltos


def hayBorde(a, n, h):

    saltos = Saltos(a, h)
    if saltos == []:
        return False
    print(saltos)

    # elimino de la lista de posiciones de saltos las posiciones que no van con el largo
    saltos_ok = []
    for g in range(len(saltos)): #recorre la lista de saltos
        if n - 1 <= saltos[g] <= (len(a) - n - 1): # si cumple con la condicion
            saltos_ok.append(saltos[g])
    print(saltos_ok)

    for k in range(len(saltos_ok)): # recorro la lista de posiciones de saltos
        m = 1   # inicializo m
        j = saltos_ok[k]
        while m < n and a[j] - a[j - m] == 0 and a[j + 1] - a[j + 1 + m] == 0:
            if m == n - 1:
                print(saltos_ok[k])
                return True
            m += 1
    return False

def EsCreciente(a):

    i = 0
    for i in range(len(a)-1):
        if a[i] > a[i+1]:
            return False
    return True

def EsDecreciente(a):

    i = 0
    for i in range(len(a)-1):
        if a[i] < a[i+1]:
            return False
    return True

def maxPos(a):

    max = a[0]
    max_pos = 0
    for i in range(len(a)):
        if a[i] > max:
            max = a[i]
            max_pos = i
    return max_pos

def listaTriangular(a):

    if a == []:
        return True

    max_pos = maxPos(a)
    termino1 = a[0: max_pos]
    termino2 = a[max_pos: ]
    if EsCreciente(termino1) == True and EsDecreciente(termino2) == True:
        return True
    return False

a = [1, 3, 4, 5]
b = [5, 2, 1]
c = [1, 2, 3, 5, 4, 2, 1]
print(maxPos(a))
print(listaTriangular(a))
print(listaTriangular(b))
print(listaTriangular(c))


# a = [1, 1, 1, 3, 3, 3, 4, 5, 8, 8, 8, 11, 11, 15, 21, 21, 30, 15, 15, 15, 4, 4, 4]
# # a = [1, 2, 4, 5]
# # saltos = Saltos(a, 3)
# # print(saltos)
# print('len(a)', len(a))
# print(hayBorde(a, 3, 11))

