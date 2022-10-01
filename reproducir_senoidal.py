import numpy as np
import matplotlib.pyplot as plt
import wave
import struct

# Se generará una señal senoidal de cierta frecuencia
# Frecuencia de la onda
frecuencia = 440
# La frecuencia de muestreo es la conversión analógica-digital
sampling_rate = float(input("Digite el numero de pruebas: "))
# Número de muestras
num_samples = int(sampling_rate)*3
# Amplitud de la onda 
amplitud = 16000
# Nombre del archivo a generar
file = "test.wav"

# Generación de la señal
sine_wave = [np.sin(2 * np.pi * frecuencia * x/sampling_rate) for x in range(num_samples)]

# PARÁMETROS PARA GENERAR EL ARCHIVO DE AUDIO
# Número de muestras
nframes=num_samples
# Tipo de compresión
comptype="NONE"
compname="not compressed"
# Número de canales
nchannels=1
# ancho del muestreo en bytes
sampwidth=2
# Abrir el archivo para su creación y escritura
wav_file=wave.open(file, 'w')
# Colocar los parámetros del archivo de audio WAV
wav_file.setparams((nchannels, sampwidth, int(sampling_rate), nframes, comptype, compname))

# Se abre el archivo y se colocan los parámetros
# struct es una librería de Python que empaqueta los datos como binarios
# el parámetro 'h' significa que es a 16 bits
for s in sine_wave:
   wav_file.writeframes(struct.pack('h', int(s*amplitud)))
wav_file.close()


