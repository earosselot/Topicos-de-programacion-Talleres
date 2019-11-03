import numpy as np
import time
import random
import sys

global N
# N = 1000


def matrizCeros():
    """genera una matriz de ceros de tamano N x N. N es una variable externa."""

    a = []
    for j in range(N):
        a.append([])
        for i in range(N):
            a[j].append(0.0)
    return a


def matrizAleatoria(a):
    """genera valores aleatorios para todas las posiciones de la matriz a"""

    tam_a = len(a)
    for j in range(tam_a):
        for i in range(tam_a):
            a[j][i] = random.random() * 5


def multMatrices(a, b, res):
    """funcion que multiplica guarda en res el resultado de la multiplicacion matricial entre a y b"""

    if isinstance(a, np.matrix):
        res = np.matmul(a, b)
    else:
        tam_c = len(res)        # guardo el tamaño de la matriz en una variable
        for i in range(tam_c):
            for j in range(tam_c):      # los dos for anteriores recorren cada posición de la matriz de resultados (res)
                for k in range(tam_c):  # este for recorre a la vez la i-esima fila de a y la j-esima columna de b y
                                        # va sumando los productos.
                    res[i][j] += a[i][k] * b[k][j]
    return


def medirTiempos(fn, *args):
    """devuelve el tiempo, en segundos, que tarda en ejecutarse la funcion(fn) con los argumentos (*args)"""

    t0 = time.time()
    fn(*args)
    t1 = time.time()
    return t1 - t0


def realizarExperimento():
    # 1) Generar 3 matrices (A, B y C) de tamano NxN
    A = matrizCeros()
    B = matrizCeros()
    C = matrizCeros()

    # 2) Completar A y B con numeros aleatorios
    matrizAleatoria(A)
    matrizAleatoria(B)

    # 3) Evaluar con medir tiempos multMatrices entre A y B y guardar en C
    tiempo_listas = medirTiempos(multMatrices, A, B, C)
    # print(C)
    print("Tiempo total listas: %f seg" % tiempo_listas)

    # 4) Generar los equivalentes de A y B en matrices de Numpy
    A_np = np.matrix(A)
    B_np = np.matrix(B)

    # 5) Reinicializar C como matriz de ceros de numpy
    C_np = np.matrix(matrizCeros())

    # 6) Evaluar con medir tiempos multMatrices entre A_np y B_np y guardar en C_np
    tiempo_np = medirTiempos(multMatrices, A_np, B_np, C_np)
    # print("C_np :", C_np)
    print("Tiempo total numpy: %f seg" % tiempo_np)


if __name__ == '__main__':
    if len(sys.argv) > 1:
        N = int(sys.argv[1])
    realizarExperimento()