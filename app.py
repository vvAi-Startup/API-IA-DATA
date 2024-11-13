#app.py
from flask import Flask
from config.db import initialize_db 
from routes.ia_data_routes import ia_data_blue_print
from flask_cors import CORS
app = Flask(__name__)

CORS(app)

initialize_db()

app.register_blueprint(ia_data_blue_print, url_prefix='/ia')

@app.route('/')
def index():
    return "Bem vindo ao Flask"

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)