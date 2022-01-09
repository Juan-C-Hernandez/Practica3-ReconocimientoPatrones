# -*- coding: utf-8 -*-
"""
Created on Sun Jan  9 14:32:07 2022

@author: juanh
"""

class Clasificador():
    
    
    def __init__(self):
        self.cuantizadores = {}
    
    
    def agregar_cuantizador(self, nombre, cuantizador):
        self.cuantizadores[nombre] = cuantizador
        pass
    
    
    def clasificar(self, x):
        dist_min = float('inf')
        dist_min_nombre = ''
        for nombre, cuantizador in self.cuantizadores.items():
            d = cuantizador.distancia_minima(x)
            if d < dist_min:
                dist_min = d
                dist_min_nombre = nombre
                
        return dist_min_nombre
                
                
            