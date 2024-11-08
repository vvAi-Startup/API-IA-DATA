#modelo/views/predict_audio
import tensorflow as tf
import numpy as np
from .audio_to_spectrogram import audio_to_spectrogram
from services.insert_data_service import save_prediction_to_db
import time

# Rodando o modelo toda vez que api for iniciada
model = tf.keras.models.load_model('./modelo/modelo_sirene_v1.0.1.h5')

# Função para fazer previsões com o modelo carregado
def predict_audio(file_path):
    try:
        if not file_path.lower().endswith(('.wav', '.mp3')):
            return {"error": "Arquivo não é de um formato de áudio válido."}
        
        start_time = time.time()
        
        spectrogram = audio_to_spectrogram(file_path)
        
        prediction = model.predict(spectrogram)
        
        end_time = time.time()
        tempo_resposta = end_time - start_time
                
        print(f'Predição bruta: {prediction}')  # Adicionado para depuração
        classes = ['ambulance', 'construction', 'dog', 'firetruck', 'traffic']
        predicted_class = classes[np.argmax(prediction)]
        
        try:
            save_prediction_to_db(predicted_class, tempo_resposta, file_path.split('/')[-1])
        except Exception as db_error:
            print(f"Erro ao salvar no banco: {db_error}")
        
        return {"predicted_class": predicted_class, "tempo_resposta": tempo_resposta}

    except Exception as e:
        print(f"Erro ao processar o áudio: {e}")
        return {"error": str(e)}
    
    
    
    
    
    