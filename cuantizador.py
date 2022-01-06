# -*- coding: utf-8 -*-
"""
Created on Wed Jan  5 17:07:25 2022

@author: juanh
"""

from procesamiento_voz import procesa_audios

class Cuantizador():
    
    def __init__(self, procesamiento_func=procesa_audios, **func_args):
        self.procesamiento_func = procesamiento_func
        self.argumentos = func_args
        pass
    
    
    def carga_archivos_entrenamiento(self, lista_nombres):
        self.procesamiento_func(lista_nombres, self.argumentos)
        pass
    
    
    def entrena(self):
        
        pass
    
    
    def compara(self):
        pass