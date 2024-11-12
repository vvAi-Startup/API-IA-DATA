# routes/ia_data_routes.py
from flask import Blueprint, request, jsonify
from models.ia_data import IAData
from datetime import datetime
from modelo.views.open_file import open_file  # Importar a função que processa o arquivo

ia_data_blue_print = Blueprint('ia_data', __name__)

@ia_data_blue_print.route('/insert_audio', methods=['POST'])
def insert_audio():
    if 'audio' not in request.files:
        return jsonify({"error": "Nenhum arquivo de áudio enviado."}), 400

    file = request.files['audio']
    
    if file.filename == '':
        return jsonify({"error": "Nenhum arquivo selecionado."}), 400

    try:
        # Chama a função que processa o arquivo de áudio
        result = open_file(file)
        
        # Verifica se o resultado contém um erro
        if "error" in result:
            return jsonify(result), 500
        
        return jsonify(result), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500


@ia_data_blue_print.route('/create_data', methods=['POST'])
def create_data():
    data = request.get_json()
    try:
        # Converter strings de data e hora para objetos datetime
        data_identificacao = datetime.strptime(data['data_identificacao'], '%Y-%m-%d').date()
        horario_identificacao = datetime.strptime(data['horario_identificacao'], '%Y-%m-%d %H:%M:%S')

        novo_dado = IAData(
            tipo_ruido=data['tipo_ruido'],
            data_identificacao=data_identificacao,
            horario_identificacao=horario_identificacao,
            tempo_resposta=data['tempo_resposta']
        )

        novo_dado.save()

        return jsonify({"message": "Dado inserido com sucesso!", "data": data}), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 400


@ia_data_blue_print.route('/datas', methods=['GET'])
def get_data():
    try:
        dados = IAData.objects()  # Recupera todos os documentos da coleção
        dados_lista = [dado.as_dict() for dado in dados]  # Usa o método as_dict()
        return jsonify(dados_lista), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 400