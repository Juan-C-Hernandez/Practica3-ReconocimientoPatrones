import voz

def procesa_audios(nombre_archivos, M=160, N=64, grado=12):
    audios = []
    for nombre in nombre_archivos:
        audios.append(voz.Voz(nombre, M, N, grado))
        
    return audios
