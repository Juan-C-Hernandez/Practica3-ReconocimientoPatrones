import numpy as np
import reconocimiento_patrones as rp


class LBG():
    
    def __init__(self, num_regiones=8):
        self.num_regiones = num_regiones        
        self._centroides = np.empty((num_regiones, 2))
        self._indice_actual = 0
        
    
    def _calcula_centroide(self, x):
        return np.mean(x, 0)
    
    
    def cuantiza(self, x, epsilon1=None, epsilon2=None, error=0.0001, dist_func=None):
        epsilon1 = epsilon1 if not epsilon1 is None else np.random.uniform(0, 0.001)
        epsilon2 = epsilon2 if not epsilon2 is None else np.random.uniform(0, 0.001)
        
        self.dist_func = dist_func if not (dist_func is None) else self._distancia_norm
        
        self._cuantiza(x, epsilon1, epsilon2, self.num_regiones, error)
    

    ############### Comprobar que el centroide es el mismo antes y después de volver a calcular cuando num_regiones = 1 ###################
    def _cuantiza(self, x,  e1, e2, num_regiones, e0):
        regiones = self._agrupa(x, e1, e2, e0)
    
        if num_regiones > 2:
            self._cuantiza(regiones[0][1], e1, e2, num_regiones / 2, e0)
            self._cuantiza(regiones[1][1], e1, e2, num_regiones / 2, e0)
            
        else:
            self._centroides[self._indice_actual] = regiones[0][0]
            self._indice_actual = self._indice_actual + 1
            self._centroides[self._indice_actual] = regiones[1][0]
            self._indice_actual = self._indice_actual + 1
    
    def centroides(self):
        return self._centroides
    
    
    def centroide_mas_cercano(self, x):
        d_min = float('inf')
        index = 0
        for i, cent in enumerate(self._centroides):
            d = self._distancia_norm(x, cent)
            if d < d_min:
                d_min = d
                index = i
                    
        return self._centroides[index]


    def _agrupa(self, x, e1, e2, e0):
        cent = self._calcula_centroide(x)
        cent1 = cent + e1
        cent2 = cent + e2
        Dgt_ant = 0
        it = 0
        r1 = []
        r2 = []
        d = []
        while True:
            Dgt = 0
            r1.clear()
            r2.clear()
            d.clear()
            for vec in x:
                #dist1 = self._distancia_norm(vec, cent1)
                #dist2 = self._distancia_norm(vec, cent2)
                dist1 = self.dist_func(vec, cent1)
                dist2 = self.dist_func(vec, cent2)
                d.append(min(dist1, dist2))
                if dist1 < dist2:
                    r1.append(vec)
                else:
                    r2.append(vec)
    
            cent1 = self._calcula_centroide(r1)
            cent2 = self._calcula_centroide(r2)
    
            Dgt = Dgt + min(d)
    
            if abs(Dgt - Dgt_ant) < e0:
                #print(f'Distancia final: {Dgt} - {Dgt_ant} - ' + str(Dgt - Dgt_ant))
                return ((cent1, r1), (cent2, r2))
    
            Dgt_ant = Dgt
            it = it + 1

    def _distancia_norm(self, x1, x2):
        return np.linalg.norm(x1 -x2)
