from flask import render_template, url_for
from app import app


@app.route("/cuidador")
def cuidador():
    return render_template("cadas_cuidador.html")