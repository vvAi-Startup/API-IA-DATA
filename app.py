from flask import Flask, request, jsonify
from config.db import client, db  # Importa a conexão com o banco de dados
from models.ia_data import IAData

app = Flask(__name__)

@app.route('/')
def index():
    return "Conectado ao MongoDB com sucesso!"

@app.route('/create_data', methods=['POST'])
def create_data():
    data = request.json
    try:
        novo_dado = IAData(
            tipo_ruido=data['tipo_ruido'],
            data_identificacao=data['data_identificacao'],
            horario_identificacao=data['horario_identificacao'],
            tempo_resposta=data['tempo_resposta']
        )
        novo_dado.save()  # Isso criará a coleção se não existir
        return jsonify({"message": "Dado inserido com sucesso!", "data": data}), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 400

if __name__ == '__main__':
    app.run(debug=True)



# import os
# from flask import Flask
# from pymongo import MongoClient
# # from config.db import Config
# from dotenv import load_dotenv

# # Carregar variáveis de ambiente do arquivo .env
# load_dotenv()

# app = Flask(__name__)
# app.config['MONGO_URI'] = os.getenv('MONGO_URI')

# # Criar uma conexão com o MongoDB
# client = MongoClient(app.config['MONGO_URI'])
# db = client.get_database()  # Obtém o banco de dados padrão
# # Config()

# @app.route('/')
# def index():
#     return "Conectado ao MongoDB com sucesso!"

# if __name__ == '__main__':
#     app.run(debug=True)
