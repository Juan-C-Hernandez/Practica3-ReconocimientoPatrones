import numpy as np
import reconocimiento_patrones as rp
import wave

class Voz():
    
    def __init__(self, nombre_archivo, M, N, grado=8):
        self.M = M
        self.N = N
        self.grado = grado
        self.vectores_r = None
        self.vectores_a = None
        self.vectores_coeficientes_wiener = None
        self.nombre = nombre_archivo
        with wave.open(nombre_archivo, 'rb') as entrada:
            self.muestras_originales = entrada.readframes(entrada.getnframes())
            #self.muestras_mono = audioop.tomono(self.muestras_originales, 2, 1, 0)
            
            #self.muestras_totales = len(self.muestras_mono)
            self.muestras_totales = len(self.muestras_originales)
            self.tiempo_total = self.muestras_totales / entrada.getframerate()
            
            #self.voz = np.frombuffer(self.muestras_mono, np.int16)
            self.voz = np.frombuffer(self.muestras_originales, np.int16)
            
            self.voz_filtro = rp.filtro_preenfasis(self.voz)
            self.ventanas = rp.forma_bloques(self.voz_filtro, M, N)
            self.ventanas_hamming = rp.ventana_hamming(self.ventanas)

    
    def vectores_a_con_vectores_r(self, vectores_r):
        vectores_a = np.empty((len(self.ventanas) + 1, len(vectores_r) + 1))
        for i, ventana in enumerate(self.ventanas_hamming):
            vectores_a[i] = rp.vectore_a(ventana, vectores_r[i])
        
        return vectores_a
       
       
    def vectores_correlacion(self):
        if self.vectores_r is None:
            self.vectores_r = np.empty((len(self.ventanas), self.grado))
            for i, ventana in enumerate(self.ventanas_hamming):
                self.vectores_r[i] = rp.vector_correlacion(self.ventana, self.grado)
                
        return self.vectores_r
        
        
    def vectores_coeficientes_wiener(self):
        if self.vectores_r is None:
            self.vectores_correlacion()
        
        if self.vectores_coeficientes_wiener is None:
            self.vectores_coeficientes_wiener = np.empty((len(self.ventanas), self.grado))
            for i, ventana in enumerate(self.ventanas_hamming):
                self.vectores_coeficientes_wiener[i] = rp.filtro_wiener(ventana, self.vectores_r[i])
                
        return self.vectores_coeficientes_wiener
    
    
    def _calcula_tiempo_ventana(self, indice_ventana):
        tiempo_inicial = self.tiempo_total * indice_ventana * self.M / self.muestras_totales
        tiempo_final = self.tiempo_total * (indice_ventana * self.M + self.N) / self.muestras_totales

        return (tiempo_inicial, tiempo_final)


    def _encuentra_ventanas_extremos(self, referencia=0.3):
        num_potencias = len(self.potencias) - 1
        inicio = 0
        fin = num_potencias
        for i in range(num_potencias):
            if self.potencias[i] > referencia:
                inicio = i
                break
    
        for i in range(i + 1, num_potencias):
            if self.potencias[i] < referencia:
                fin = i - 1
                break

        return (inicio, fin)
    
    
    def __str__(self):
        return f"Nombre: {self.nombre}\nDuración: {self.tiempo_total}"


    def __repr__(self):
        return f'Voz(nombre={self.nombre}, duración={self.tiempo_total}, M={self.M}, N={self.N}, grado={self.grado}'
