from flask import redirect, url_for, request, flash
from app import app
from app.models.geral import *

@app.route("/proce", methods=['POST'])
def pro():
    nome = request.form.get('nome', '').strip()
    data = request.form.get('data_nascimento', '').strip()
    numerar = request.form.get('cpf', '').strip() #o numerar seria o cpf
    genero = request.form.get('genero', '').strip()
    endereco = request.form.get('endereco', '').strip()
    telefone = request.form.get('telefone', '').strip()
    
    if not nome or not data or not numerar:
        flash("Preencha todos os campos obrigatórios")
        return redirect(url_for('cadastro'))
    if nome and data and numerar:
        
        nov_c = Cadastro(nome,data, numerar,genero,endereco,telefone)
        nov_c.adicionar()
        return redirect(url_for('home'))

@app.route("/proce_cuidador", methods=["POST"])
def pro_cuidador():
    nome = request.form.get("nome", "").strip()
    data = request.form.get("data_nascimento", "").strip()
    cpf = request.form.get("cpf", "").strip()
    genero = request.form.get("genero", "").strip()
    endereco = request.form.get("endereco", "").strip()
    telefone = request.form.get("telefone", "").strip()

    if not nome or not data or not cpf:
        flash("Preencha todos os campos obrigatórios")
        return redirect(url_for("cuidador"))

    novo = Cuidador(nome, data, cpf, genero, endereco, telefone)
    novo.adicionar()
    flash("Cadastro de cuidador realizado com sucesso!")
    return redirect(url_for("home"))




