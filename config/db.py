import os
from pymongo import MongoClient
from dotenv import load_dotenv
from mongoengine import connect
# Carregar variáveis de ambiente do arquivo .env
load_dotenv()

# Obter a URI do MongoDB do arquivo .env
MONGO_URI = os.getenv("MONGO_URI")

def initialize_db():
    """Inicializa a conexão com o banco de dados MongoDB."""
    connect(host=MONGO_URI)
    print('Conectado ao MongoDB com sucesso!')



# # Criar uma conexão com o MongoDB
# client = MongoClient(MONGO_URI)
# db = client.get_default_database()  # Obtém o banco de dados padrão
# print('Conectado ao Mongo com Sucesso!')
