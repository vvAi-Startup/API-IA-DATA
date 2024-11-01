from flask import Flask, request, jsonify
from config.db import client, db  # Importa a conexão com o banco de dados
from models.ia_data import IAData
from datetime import datetime
from dotenv import load_dotenv
import os
from mongoengine import connect
load_dotenv()
MONGO_URI = os.getenv("MONGO_URI")
connect(host=MONGO_URI)

app = Flask(__name__)
@app.route('/')
def index():
    return "Bem vindo ao Flask"

@app.route('/create_data', methods=['POST'])
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


if __name__ == '__main__':
    app.run(debug=True)

