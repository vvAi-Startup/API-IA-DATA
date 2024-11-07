from models.ia_data import IAData

def save_prediction_to_db(tipo_ruido, tempo_resposta):
    """Função para salvar a predição da IA no banco de dados."""
    try:
        ia_data = IAData(tipo_ruido=tipo_ruido, tempo_resposta=tempo_resposta)
        ia_data.save()  # Salva os dados no banco de dados
        print("Dados salvos com sucesso!")
    except Exception as e:
        print(f"Erro ao salvar os dados no banco: {e}")
