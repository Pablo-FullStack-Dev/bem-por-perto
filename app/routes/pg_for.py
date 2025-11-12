
from flask import render_template, url_for
from app import app

@app.route("/cadastro")
def cadastro():
    return render_template("/cliente/formulario.html")