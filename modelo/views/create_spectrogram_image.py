#modelo/views/create_espectrogram_image
import librosa
import numpy as np
import matplotlib.pyplot as plt
plt.use('Agg')
import os
import base64

# Função para criar e salvar a imagem do espectrograma
def create_spectrogram_image(file_path, output_dir='uploads/spectrograms/'):
    # Garantir que o diretório de saída existe
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    
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

     # Extrair o nome do arquivo sem a extensão
    base_filename = os.path.splitext(os.path.basename(file_path))[0]
    output_path = os.path.join(output_dir, f'{base_filename}.png')
    
    # Salvar a imagem em um objeto BytesIO
    plt.savefig(output_path, format='png', bbox_inches='tight', pad_inches=0)
    plt.close()

     # Converter a imagem salva para base64
    with open(output_path, "rb") as image_file:
        base64_image = base64.b64encode(image_file.read()).decode('utf-8')
    
    return output_path, base64_image