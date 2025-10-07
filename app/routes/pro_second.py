from flask import redirect, url_for, request, flash
from app.models import *
from app import app

@app.route("/proce", methods=['POST'])
def pro():
    nome = request.form.get('nome', '').strip()
    data = request.form.get('data_nascimento', '').strip()
    numerar = request.form.get('cpf', '').strip() #o numerar seria o cpf

    if not nome or not data or not numerar:
        flash("Preencha todos os campos obrigatórios")
        return redirect(url_for('cadastro'))
    if nome and data and numerar:
        return redirect(url_for('home'))




