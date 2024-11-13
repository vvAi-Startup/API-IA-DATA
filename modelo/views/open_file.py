from .predict_audio import predict_audio
from .create_spectrogram_image import create_spectrogram_image
from .create_waveform_image import create_waveform_image
import io
import base64
import tempfile
import os

def open_file(file):
    """
    Função que recebe um arquivo de áudio enviado pelo frontend,
    faz a predição e gera as imagens do espectrograma e da forma de onda,
    e retorna os resultados em formato JSON.
    """
    try:
       # Usando o diretório temporário do sistema (Windows ou Linux)
        temp_dir = tempfile.gettempdir()  # Diretório temporário do sistema
        file_path = os.path.join(temp_dir, file.filename)
        file.save(file_path)

        # 1. Fazer a predição do áudio
        result = predict_audio(file_path)

        # 2. Gerar o espectrograma como imagem
        spectrogram_img = create_spectrogram_image(file_path)
        spectrogram_img_io = io.BytesIO()
        spectrogram_img.save(spectrogram_img_io, format="PNG")
        spectrogram_img_io.seek(0)
        spectrogram_base64 = base64.b64encode(spectrogram_img_io.getvalue()).decode("utf-8")

        # 3. Gerar a forma de onda como imagem
        waveform_img = create_waveform_image(file_path)
        waveform_img_io = io.BytesIO()
        waveform_img.save(waveform_img_io, format="PNG")
        waveform_img_io.seek(0)
        waveform_base64 = base64.b64encode(waveform_img_io.getvalue()).decode("utf-8")

        # 4. Retornar os resultados em formato JSON
        return {
            "predicted_class": result,  # A predição do áudio
            "spectrogram": spectrogram_base64,  # Spectrograma em base64
            "waveform": waveform_base64  # Forma de onda em base64
        }

    except Exception as e:
        # Retornar erro em caso de falha
        return {"error": str(e)}
