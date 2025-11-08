# Entenda esse arquivo como se fosse a cozinha
# a demais pastas seria o armazem aonde se encontra os ingredientes
from flask import Flask
# from flask_mysqldb import MySQL
# from dotenv import load_dotenv
# import os

# carrega as variáveis do .env (senha, banco etc.)
# load_dotenv()

app = Flask(__name__)  

# app.secret_key = os.getenv("SECRET_KEY", "chave_padrao_insegura")

# # configurações do MySQL (vêm do arquivo .env)
# app.config["MYSQL_HOST"] = os.getenv("DB_HOST", "localhost")
# app.config["MYSQL_USER"] = os.getenv("DB_USER", "root")
# app.config["MYSQL_PASSWORD"] = os.getenv("DB_PASSWORD", "")
# app.config["MYSQL_DB"] = os.getenv("DB_NAME", "bemporperto")
# app.config["MYSQL_PORT"] = int(os.getenv("DB_PORT", 3306))

# # inicializa o MySQL
# mysql = MySQL(app)


from app.routes import * #esse seria o caminho para poder chegar até os ingredientes
# from .models import models


