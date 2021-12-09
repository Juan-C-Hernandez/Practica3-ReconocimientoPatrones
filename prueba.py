import numpy as np
import matplotlib.pyplot as plt
import reconocimiento_patrones as rp
from LBG_alg import LBG
from math import inf

def distancia_norm(x1, x2):
        return np.linalg.norm(x1 -x2)

pares = np.random.uniform(0, 100, (2000, 2))

n_regiones = 32
lbg = LBG(num_regiones=n_regiones)
lbg.cuantiza(pares)

regiones = dict()
for c in lbg.centroides():
    regiones[str(c)] = list()

for par in pares:
    c = lbg.centroide_mas_cercano(par)
    regiones[str(c)].append(par)

for k, region in regiones.items():
    region = np.asarray(region)
    plt.scatter(region[:,0], region[:,1])
plt.scatter(lbg.centroides()[:,0], lbg.centroides()[:,1], color='black')


plt.show()
