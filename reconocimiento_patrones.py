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


def correlacion_corta(x, i):
    """
        suma de k = 0 a N-i de x_k * x_{k+i}
    """
    lim_sup = len(x) - abs(i)
    suma = 0
    for i in range(lim_sup):
        suma += x[i] * x[i + i]
    
    return suma


def funcion_correlacion(x, i):
    """
        Función de correlación
        r(s) = 1/N * sum de k = 0 a N-1 de x_k * x_{k + 1}
    """

    return correlacion_corta(x, i) / len(x)


def vector_correlacion(x, num_coeficientes):
    vector = np.empty(num_coeficientes)
    for i in range(num_coeficientes):
        # i + 1 porque el vector correlación no contempla i = 0
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


def distancia_Itakura_Saito(vector1, vector2, sigma=1):
    #distancia = 0
    #for i in range(1, len(r_corta)):
        #distancia += r_corta[i] * correlaciones[i]
    #distancia = (distancia * 2) + (r_corta[0] * correlaciones[0]) 
    ##print('Distancia: ', distancia)
    ##print('r_corta ', r_corta)
    ##print('correlaciones ', correlaciones)
    #return distancia

    return (vector1[0] * vector2[0] + 2 * np.dot(vector1, vector2)) / (sigma * sigma)
    
    
def potencia(x):
    return funcion_correlacion(x, 0)
