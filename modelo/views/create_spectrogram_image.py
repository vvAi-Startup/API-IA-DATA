#modelo/views/create_espectrogram_image
import librosa
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image, ImageTk
import io

# Função para criar e salvar a imagem do espectrograma
def create_spectrogram_image(file_path):
    y, sr = librosa.load(file_path, sr=None)
    spectrogram = librosa.feature.melspectrogram(y=y, sr=sr)
    
    # Padronizar o comprimento do espectrograma
    if spectrogram.shape[1] > 128:
        spectrogram = spectrogram[:, :128]
    else:
        padding = 128 - spectrogram.shape[1]
        spectrogram = np.pad(spectrogram, ((0, 0), (0, padding)), mode='constant')
    
    # Criar a imagem do espectrograma
    plt.figure(figsize=(6, 3))
    plt.imshow(librosa.power_to_db(spectrogram, ref=np.max), aspect='auto', cmap='inferno')
    plt.axis('off')
    
    # Salvar a imagem em um objeto BytesIO
    buf = io.BytesIO()
    plt.savefig(buf, format='png', bbox_inches='tight', pad_inches=0)
    plt.close()
    
    buf.seek(0)
    image = Image.open(buf)
    return ImageTk.PhotoImage(image)