#modelo/views/create_waveform_image
import librosa
import matplotlib.pyplot as plt
import numpy as np
from PIL import Image, ImageTk
import io

# Função para criar e salvar a imagem da forma de onda do áudio
def create_waveform_image(file_path):
    y, sr = librosa.load(file_path, sr=None)
    plt.figure(figsize=(6, 2))
    plt.plot(np.linspace(0, len(y) / sr, num=len(y)), y)
    plt.title('Forma de Onda do Áudio')
    plt.xlabel('Tempo (s)')
    plt.ylabel('Amplitude')
    plt.grid()
    
    # Salvar a imagem em um objeto BytesIO
    buf = io.BytesIO()
    plt.savefig(buf, format='png', bbox_inches='tight', pad_inches=0)
    plt.close()
    
    buf.seek(0)
    image = Image.open(buf)
    return ImageTk.PhotoImage(image)