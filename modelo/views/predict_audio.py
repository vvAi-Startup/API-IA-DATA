#modelo/views/predict_audio
import tensorflow as tf
import numpy as np
from .audio_to_spectrogram import audio_to_spectrogram
from services.insert_data_service import save_prediction_to_db
import time

# Função para fazer previsões com o modelo carregado
def predict_audio(file_path):
    try:
        start_time = time.time()
        
        spectrogram = audio_to_spectrogram(file_path)
        model = tf.keras.models.load_model('./modelo/modelo_sirene_v1.0.1.h5')
        prediction = model.predict(spectrogram)
        
        end_time = time.time()
        tempo_resposta = end_time - start_time
                
        print(f'Predição bruta: {prediction}')  # Adicionado para depuração
        classes = ['ambulance', 'construction', 'dog', 'firetruck', 'traffic']
        predicted_class = classes[np.argmax(prediction)]
        
        save_prediction_to_db(predicted_class, tempo_resposta)
        
        return predicted_class
    except Exception as e:
        print(f"Erro ao processar o áudio: {e}")
        return None