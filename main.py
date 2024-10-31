from flask import Flask
from routes import initialize_routes



app = Flask(__name__)

app.run()