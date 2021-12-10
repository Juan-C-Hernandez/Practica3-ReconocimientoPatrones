import numpy as np
import reconocimiento_patrones as rp
import procesamiento_voz as pv


if __name__ == '__main__':
    nombres = pv.obtiene_nombres_archivos()
    print(f"Se encontraron {len(nombres)} archivos:")
    for nombre in nombres:
        print(nombre)
    audios = pv.procesa_audio(nombres, 10, 12, 8)
    for audio in audios:
        print(str(audio))
