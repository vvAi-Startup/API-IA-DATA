#modelo/views/create_espectrogram_image
import librosa
import numpy as np
import matplotlib.pyplot as plt

# Função para criar e salvar a imagem do espectrograma
def create_spectrogram_image(file_path, output_dir='uploads/spectrograms/'):
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
    output_path = f'{output_dir}{file_path.split("/")[-1]}.png'
    plt.savefig(output_path, format='png', bbox_inches='tight', pad_inches=0)
    plt.close()
    
    return output_path