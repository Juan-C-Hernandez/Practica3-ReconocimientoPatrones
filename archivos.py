# -*- coding: utf-8 -*-
"""
Created on Wed Jan  5 17:58:03 2022

@author: juanh
"""

import os

def nombres_archivos(path, ext):
    print("path: " +  path)
    archivos = os.listdir(path)
    return [x for x in archivos if x.endswith(ext)]


def obtiene_nombres_archivos():
    archivos_finales = set()
    while True:
        sel = input("Buscar archivos en directorio actual? [S/n]: ")
        ruta = '.'
        if sel == 'n' or sel == 'N':
            ruta = input("Escribe la ruta: ")
        
        ext = input("extensión de archivo: ")
        
        nombres = nombres_archivos(ruta, ext)
        print(f"Se encontraron {len(nombres)} archivos con extensión {ext}:")
        for nombre in nombres:
            print(nombre)
            
        sel = input("Añadir archivos? [S/n]: ")
        if sel == 'n' or sel == 'N':
            continue
    
        archivos_finales.update(nombres)
    
        sel = input("Agregar mas archivos? [s/N]: ")
        if not (sel == 'S' or sel == 's'):
            return archivos_finales
