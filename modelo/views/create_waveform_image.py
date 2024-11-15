#modelo/views/create_waveform_image
import librosa
import matplotlib.pyplot as plt
import numpy as np
import os
import base64
# Função para criar e salvar a imagem da forma de onda do áudio
def create_waveform_image(file_path, output_dir='uploads/waveforms/'):
    # Garantir que o diretório de saída existe
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    
    y, sr = librosa.load(file_path, sr=None)
    plt.figure(figsize=(6, 2))
    plt.plot(np.linspace(0, len(y) / sr, num=len(y)), y)
    plt.title('Forma de Onda do Áudio')
    plt.xlabel('Tempo (s)')
    plt.ylabel('Amplitude')
    plt.grid()
    
    # Extrair o nome do arquivo sem a extensão
    base_filename = os.path.splitext(os.path.basename(file_path))[0]
    output_path = os.path.join(output_dir, f'{base_filename}.png')
    
    
    # Salvar a imagem no diretório
    try:
        plt.savefig(output_path, format='png', bbox_inches='tight', pad_inches=0)
    except Exception as e:
        print(f"Erro ao salvar a imagem da forma de onda: {e}")

    plt.close()

    # Verifique se a imagem foi salva corretamente
    if not os.path.exists(output_path):
        print(f"Imagem não salva corretamente no caminho: {output_path}")
        return None

    # Converter a imagem salva para base64
    try:
        with open(output_path, "rb") as image_file:
            base64_image = base64.b64encode(image_file.read()).decode('utf-8')
    except Exception as e:
        print(f"Erro ao converter a imagem da forma de onda para base64: {e}")
        base64_image = None
    
    return output_path, base64_image