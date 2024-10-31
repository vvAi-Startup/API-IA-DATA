import os

class Config:
    # Use a URI do MongoDB Atlas com o nome do banco de dados
    MONGO_URI = os.getenv("MONGO_URI", "mongodb+srv://<username>:<password>@cluster0.mongodb.net/mydatabase?retryWrites=true&w=majority")
