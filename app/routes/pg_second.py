from flask import render_template, request, url_for, redirect, flash

from app import app
from ..models import *
from .pg_one import *


@app.route("/login")
def login():
    return render_template("login.html")



@app.route("/ver", methods=['POST'])
def veriq():
    email = request.form.get('email', '').strip()
    senha = request.form.get('p_v', '').strip()

    usr = Comandos()

    if usr.verificar(email, senha):
        print("conta conectada")
        return redirect(url_for('home'))
    else:
        flash("Erro com email ou senha")
        return redirect(url_for('login'))



