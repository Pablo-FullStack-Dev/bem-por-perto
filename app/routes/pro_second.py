from flask import redirect, url_for, request, flash
from app import app
from ..models import *
from .pg_one import *


@app.route("/proce", methods=['POST']) # essa rota está direcionada a tabela Usuario
def cadas():
    nome = request.form.get('nome', '').strip()
    idade = request.form.get('idade', '').strip() # adicionando a variavel idade. 25/11/2025
    dia = request.form.get("dia", "").strip()
    mes =  request.form.get("mes", "").strip()
    ano = request.form.get("ano", "").strip()
    cpf = request.form.get('cpf', '').strip() #o numerar seria o cpf
    genero = request.form.get('genero', '').strip()
    endereco = request.form.get('endereco', '').strip()
    cep = request.form.get('cep', '').strip()
    
    telefone = request.form.get('telefone', '').strip()
    email = request.form.get('email', '').strip() # foi adicionado dia 25/ de novembro
    passe = request.form.get('passe', '').strip() # foi adicionado dia 25/ de novembro

    # agr é colocar as infomações na POO e adicionar +1 função na POO

# ============================================================

    if not nome or not idade or not dia or not mes or not ano or not cpf or not genero or not endereco or not telefone or not email:
        flash("Preencha todos os campos obrigatórios")
        return redirect(url_for('cadastro'))
    elif nome and idade and dia and mes and ano and cpf and genero and endereco and telefone and email:
        novo_usuario = Comandos()
        if novo_usuario.adicionar(n=nome,i=idade,dia=dia,mes=mes,ano=ano,cf=cpf,g=genero,ed=endereco,ce=cep,te=telefone,e=email, senha=passe):

            print("\nDados adicionados!!!\n")
            return redirect(url_for('home')) # agr as informações estaos sendo captadas.
# ////////////////////////////////////////////////////////////////////////////////////////



















































@app.route("/proce_cuidador", methods=["POST"])
def pro_cuidador():
    nome = request.form.get("nome", "").strip()
    data = request.form.get("data_nascimento", "").strip()
    
    email = request.form.get("email", "").strip()
    genero = request.form.get("genero", "").strip()
    endereco = request.form.get("endereco", "").strip()
    telefone = request.form.get("telefone", "").strip()
    formacao = request.form.get("formacao", "").strip()


    if not nome or not data or not email:
        flash("Preencha todos os campos obrigatórios")
        return redirect(url_for("cuidador"))

    # novo = Cuidador(nome, data, email, genero, endereco, telefone, formacao)
    # novo.adicionar()
    flash("Cadastro de cuidador realizado com sucesso!")
    return redirect(url_for("home"))




