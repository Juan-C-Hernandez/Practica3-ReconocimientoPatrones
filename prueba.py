import numpy as np
import reconocimiento_patrones as rp

def correlacion_corta(vector_a):
    ra = []
    for i in range(0, len(vector_a)-1):
        rai = 0
        for j in range(0, len(vector_a)-1-i):
            rai = rai + vector_a[j] * vector_a[j+i]
        ra.append(rai)
    return ra 


def suma_correlacion(vector, i):
    suma = 0
    for i in range(len(vector - i)):
        suma = vector[i] * vector[i + 1]
    
    return suma



def funcion_correlacion_2(vector, i):
    rai = 0
    for j in range(0, len(vector)-1-i):
        rai = rai + vector[j] * vector[j+i]
    return rai

def distancia_norm(x1, x2):
        return np.linalg.norm(x1 -x2)

pares = np.random.uniform(0, 100, 100)

correlacion_normal = rp.funcion_correlacion(pares, 4)
correlacion_2 = funcion_correlacion_2(pares, 4)
print(len(pares) * correlacion_normal)
print(correlacion_2)
