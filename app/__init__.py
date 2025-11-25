# Entenda esse arquivo como se fosse a cozinha
# a demais pastas seria o armazem aonde se encontra os ingredientes
from flask import Flask
# from flask_mysqldb import MySQL
# from dotenv import load_dotenv
# import os

# carrega as variáveis do .env (senha, banco etc.)
# load_dotenv()

app = Flask(__name__)  

app.secret_key = "ksksks"



from app.routes import * #esse seria o caminho para poder chegar até os ingredientes
# from .models import models


