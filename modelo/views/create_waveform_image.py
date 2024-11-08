#modelo/views/create_waveform_image
import librosa
import matplotlib.pyplot as plt
import numpy as np
from PIL import Image, ImageTk
import io

# Função para criar e salvar a imagem da forma de onda do áudio
def create_waveform_image(file_path, output_dir='uploads/waveforms/'):
    y, sr = librosa.load(file_path, sr=None)
    plt.figure(figsize=(6, 2))
    plt.plot(np.linspace(0, len(y) / sr, num=len(y)), y)
    plt.title('Forma de Onda do Áudio')
    plt.xlabel('Tempo (s)')
    plt.ylabel('Amplitude')
    plt.grid()
    
    # Salvar a imagem no diretório
    output_path = f'{output_dir}{file_path.split("/")[-1]}.png'
    plt.savefig(output_path, format='png', bbox_inches='tight', pad_inches=0)
    plt.close()
    
    return output_path