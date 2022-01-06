import voz

def procesa_audios(nombre_archivos, M, N, grado):
    audios = []
    for nombre in nombre_archivos:
        audios.append(voz.Voz(nombre, M, N, grado))
        
    return audios
