import os
from pymongo import MongoClient
from dotenv import load_dotenv

# Carregar variáveis de ambiente do arquivo .env
load_dotenv()

# Obter a URI do MongoDB do arquivo .env
MONGO_URI = os.getenv("MONGO_URI")

# Criar uma conexão com o MongoDB
client = MongoClient(MONGO_URI)
db = client.get_default_database()  # Obtém o banco de dados padrão
print('Conectado ao Mongo com Sucesso!')
