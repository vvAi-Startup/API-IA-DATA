#app.py
from flask import Flask
from config.db import initialize_db 
from routes.ia_data_routes import ia_data_blue_print

app = Flask(__name__)

initialize_db()

app.register_blueprint(ia_data_blue_print, url_prefix='/ia')

@app.route('/')
def index():
    return "Bem vindo ao Flask"

if __name__ == '__main__':
    app.run(debug=True)