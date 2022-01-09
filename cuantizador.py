# -*- coding: utf-8 -*-
"""
Created on Wed Jan  5 17:07:25 2022

@author: juanh
"""
import archivos
from procesamiento_voz import procesa_audios
import reconocimiento_patrones as rp
import numpy as np
import lbg

class Cuantizador():
    
    def __init__(self, num_regiones=8):
        self.cuantizador = None
        self.objetos_procesados = None
        self.num_regiones = num_regiones
        self.cuantizador = None
    
    
    def cargar_archivos_entrenamiento_helper(self):
        nombres_archivos = archivos.obtiene_nombres_archivos()
        self.carga_archivos_entrenamiento(nombres_archivos)
    
    
    def carga_archivos_entrenamiento(self, lista_nombres, procesamiento_func=procesa_audios, **func_args):
        self.objetos_procesados = procesamiento_func(lista_nombres, func_args)
    
    
    def entrena(self):
        self.cuantizador = lbg.LBG(self.num_regiones)
        coeficientes = []
        for objeto in self.objetos_procesados:
            coeficientes.append(objeto.vectores_coeficientes_wiener())
            
        coeficientes = np.toarray(coeficientes)
        self.cuantizador.cuantiza(coeficientes, dist_func=rp.distancia_Itakura_Saito)
    
    
    def distancia_minima(self, x):
        if self.cuantizador is None:
            return None
        
        return self.cuantizador.centroide_mas_cercano_y_distancia(x)[1]