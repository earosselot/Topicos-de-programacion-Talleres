import numpy as np
import time
import random
import sys

global N
N = 100

def matrizCeros():
    """genera una matriz de ceros usando de tamaño N x N. N es una variable externa."""

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
            a[j][i] = int(random.random()*5)


def multMatrices(a, b, res):
    """función que multiplica guarda en res el resultado de la multiplicación matricial entre a y b"""

    if isinstance(a, np.matrix):
        print(np.matmul(a, b))   # res NO GUARDA LA MULTIPLICACION, NO SE PORQUE...
    else:
        tam_c = len(res)
        for i in range(tam_c):
            for j in range(tam_c):
                for k in range(tam_c):
                    res[i][j] += a[i][k] * b[k][j]


def medirTiempos(fn, *args):
    """devuelve el tiempo, en segundos, que tarda en ejecutarse la funcion(fn) con los argumentos (*args)"""

    t0 = time.time()
    fn(*args)
    t1 = time.time()
    return t1 - t0


def realizarExperimento():

    # 1) Generar 3 matrices (A, B y C) de tamaño NxN
    A = matrizCeros()
    B = matrizCeros()
    C = matrizCeros()

    # 2) Completar A y B con numeros aleatorios
    matrizAleatoria(A)
    matrizAleatoria(B)

    # 3) Evaluar con medir tiempos multMatrices entre A y B y guardar en C
    tiempo_listas = medirTiempos(multMatrices, A, B, C)
    print(C)
    print("Tiempo total listas: %f.5" % tiempo_listas)

    # 4) Generar los equivalentes de A y B en matrices de Numpy
    A_np = np.matrix(A)
    B_np = np.matrix(B)

    # 5) Reinicializar C como matriz de ceros de numpy
    C_np = np.matrix(matrizCeros())

    # 6) Evaluar con medir tiempos multMatrices entre A_np y B_np y guardar en C_np
    tiempo_np = medirTiempos(multMatrices, A_np, B_np, C_np)
    # print(C_np)
    print("Tiempo total numpy: %f.5" % tiempo_np)

realizarExperimento()

# if __name__ == '__main__':
#     if len(sys.argv) > 1:
#         N = int(sys.argv[1])
#     realizarExperimento()
