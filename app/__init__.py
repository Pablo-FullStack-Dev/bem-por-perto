# Entenda esse arquivo como se fosse a cozinha
# a demais pastas seria o armazem aonde se encontra os ingredientes
from flask import Flask, url_for


app = Flask(__name__)  
app.secret_key = 'segredo'



from app.routes import * #esse seria o caminho para poder chegar até os ingredientes