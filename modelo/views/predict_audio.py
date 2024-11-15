# modelo/views/predict_audio
import asyncio
import tensorflow as tf
import numpy as np
from .audio_to_spectrogram import audio_to_spectrogram
from services.insert_data_service import save_prediction_to_db
from .create_spectrogram_image import create_spectrogram_image
from .create_waveform_image import create_waveform_image
import time
import base64

# Rodando o modelo toda vez que api for iniciada
model = tf.keras.models.load_model('./modelo/modelo_sirene_v1.0.1.h5')

async def audio_to_base64(file_path):
    """Converte o arquivo de áudio para base64"""
    with open(file_path, "rb") as audio_file:
        return base64.b64encode(audio_file.read()).decode('utf-8')

# Função para fazer previsões com o modelo carregado
async def predict_audio(file_path):
    try:
        if not file_path.lower().endswith(('.wav', '.mp3')):
            return {"error": "Arquivo não é de um formato de áudio válido."}

        start_time = time.time()

        # Converte o áudio em base64
        audio_base64 = await asyncio.to_thread(audio_to_base64,file_path)

        spectrogram = await asyncio.to_thread(audio_to_spectrogram, file_path)

        prediction = await asyncio.to_thread(model.predict, spectrogram)

        end_time = time.time()
        tempo_resposta = end_time - start_time

        print(f'Predição bruta: {prediction}')  # Adicionado para depuração
        classes = ['ambulance', 'construction', 'dog', 'firetruck', 'traffic']
        predicted_class = classes[np.argmax(prediction)]

        # Criar imagens e obter base64
        spectrogram_path, spectrogram_base64 = await asyncio.to_thread(create_spectrogram_image, file_path)
        waveform_path, waveform_base64 = await asyncio.to_thread(create_waveform_image, file_path)

        # Simular vetor do áudio convertido (adapte para seu caso)
        # audio_vector = spectrogram.flatten().tolist()

        try:
            saved_id = await asyncio.to_thread(save_prediction_to_db,
                predicted_class,
                tempo_resposta,
                file_path.split('/')[-1],
                audio_base64,
                spectrogram_base64,
                waveform_base64
                )

            
            print(f"Predição salva no banco de dados com o ID: {saved_id}")
        except Exception as db_error:
            print(f"Erro ao salvar no banco: {db_error}")

        return {
            "predicted_class": predicted_class,
            "tempo_resposta": tempo_resposta,
            "saved_id": saved_id,
            "spectrogram": spectrogram_base64,
            "waveform": waveform_base64
            }

    except Exception as e:
        print(f"Erro ao processar o áudio: {e}")
        return {"error": str(e)}
