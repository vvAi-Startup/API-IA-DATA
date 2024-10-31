from flask import Flask
from pymongo import MongoClient
import os
from dotenv import load_dotenv

# Carregar variáveis de ambiente do arquivo .env
load_dotenv()

app = Flask(__name__)

# Obter a URI do MongoDB do arquivo .env
app.config['MONGO_URI'] = os.getenv('MONGO_URI')

# Criar uma conexão com o MongoDB
client = MongoClient(app.config['MONGO_URI'])
db = client.get_default_database()  # Obtém o banco de dados padrão

@app.route('/')
def index():
    return "Conectado ao MongoDB com sucesso!"

if __name__ == '__main__':
    app.run(debug=True)
