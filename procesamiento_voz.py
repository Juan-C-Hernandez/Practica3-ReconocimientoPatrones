import voz
import os

def nombres_archivos(path, ext):
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


def procesa_audios(nombre_archivos, M, N, grado):
    audios = []
    for nombre in nombre_archivos:
        audios.append(voz.Voz(nombre, M, N, grado))
        
    return audios
