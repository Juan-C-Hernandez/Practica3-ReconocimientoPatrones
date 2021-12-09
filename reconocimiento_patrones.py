import numpy as np

def filtro_preenfasis(x):
    """
        Filtro h(z) = 1 - 0.95z^-1
    """
    salida = np.empty(len(x))
    salida[0] = x[0]
    for n in range(1, len(x)):
        salida[n] = x[n] - 0.95 * x[n - 1]

    return salida


def funcion_correlacion(x, sigma):
    """
        Función de correlación
        r(s) = 1/N * sum de i = 0 a N-1 de x_i * x_{i+s}
    """
    sigma = abs(sigma)
    N = len(x)
    lim_sup = N - sigma
    suma = 0
    for i in range(lim_sup):
        suma += x[i] * x[i + sigma]

    return suma / N


def vector_correlacion(x, num_coeficientes):
    vector = np.empty(num_coeficientes)
    for i in range(num_coeficientes):
        vector[i] = funcion_correlacion(x, i + 1)

    return vector


def matriz_correlacion(x, r):
    M = len(r)
    R = np.empty((M, M))
    r0 = funcion_correlacion(x, 0)
    for i in range(M):
        R[i][i]= r0
        for j in range(1, M - i):
            R[i][i + j] = r[j - 1]
            R[i + j][i] = r[j - 1]

    return  R


def filtro_Wiener(x, r):
    R = matriz_correlacion(x, r)
    return  np.dot(np.linalg.inv(R), r)



def vector_a(x, r):
    """
        Crea el vector a = [1 - w]
    """
    R = matriz_correlacion(x, r)
    coeficientes_wiener = filtro_Wiener(R, r)
    a = np.empty(len(coeficientes_wiener) + 1)
    a[0] = 1
    a[1:] = -coeficientes_wiener

    return a


def forma_bloques(x, M, N):
    ventanas = []
    l = 0
    while M * l + N < len(x):
        ventanas.append(x[M * l: M * l + N])
        l = l + 1

    return np.asarray(ventanas)


def ventana_hamming(ventanas):
    ventanas_hamming = np.empty_like(ventanas, dtype=float)
    N = len(ventanas[0])
    for i in range(len(ventanas)):
        ventanas_hamming[i] = 0.54 - 0.4 * np.cos(2 * np.pi * ventanas[i] / (N - 1))

    return ventanas_hamming


def distancia_Itakura_Saito(a, b):
    


def potencia(x):
    return funcion_correlacion(x, 0)
