from models.ia_data import IAData

def save_prediction_to_db(tipo_ruido, tempo_resposta, nome_audio, spectrogram_base64, waveform_base64, vetor_audio_base64):
    """Função para salvar a predição da IA no banco de dados."""
    try:
        ia_data = IAData(tipo_ruido=tipo_ruido, tempo_resposta=tempo_resposta, nome_audio=nome_audio,  spectrograma_cripto=spectrogram_base64,
            waveform_cripto=waveform_base64,
            vetor_audio=vetor_audio_base64)
        ia_data.save()  # Salva os dados no banco de dados
        saved_id = str(ia_data.id)
        print(f"Dados salvos com sucesso! ID:{saved_id}")
        return saved_id
    except Exception as e:
        print(f"Erro ao salvar os dados no banco: {e}")
