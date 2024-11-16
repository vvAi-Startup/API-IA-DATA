# modelo/views/create_espectrogram_image
import librosa
import numpy as np
import matplotlib.pyplot as plt
import os
import base64

# Função para criar e salvar a imagem do espectrograma


def create_spectrogram_image(file_path, output_dir='uploads/spectrograms/'):
    try:
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
            spectrogram = np.pad(
                spectrogram, ((0, 0), (0, padding)), mode='constant')

        # Criar a imagem do espectrograma
        plt.figure(figsize=(6, 3))
        plt.imshow(librosa.power_to_db(spectrogram, ref=np.max),
                aspect='auto', cmap='inferno')
        plt.axis('off')

        # Extrair o nome do arquivo sem a extensão
        base_filename = os.path.splitext(os.path.basename(file_path))[0]
        output_path = os.path.join(output_dir, f'{base_filename}.png')

        # Salvar a imagem em um objeto BytesIO
        plt.savefig(output_path, format='png', bbox_inches='tight', pad_inches=0)
        plt.close()

        # Verificação se a imagem foi salva corretamente
        if not os.path.exists(output_path):
            raise Exception(
                f"Erro ao salvar a imagem do espectrograma no caminho: {output_path}")

        # Converter a imagem salva para base64
        with open(output_path, "rb") as image_file:
            base64_image = base64.b64encode(image_file.read()).decode('utf-8')

        if not base64_image:
            raise Exception("Erro ao converter a imagem para base64.")

        return output_path, base64_image


    except Exception as e:
        # Logar o erro e lançar uma exceção
        print(f"Erro ao criar espectrograma: {e}")
        return None, None
