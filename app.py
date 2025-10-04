from flask import Flask, render_template, request, flash, redirect


app = Flask(__name__)  

@app.route("/inicial")
def inicial():
    return render_template("index.html")

@app.route("/sobre")
def sobre():
    return render_template("sobre.html")

@app.route("/cuidador")
def cuidador():
    return render_template("cadas_cuidador.html")

@app.route("/ajuda")
def ajuda():
    return render_template("ajuda.html")

@app.route("/login")
def login():
    return render_template("login.html")

@app.route("/cadastro")
def cadastro():
    return render_template("cadas.html")

@app.route("/explorar")
def explorar():
    return render_template("explorar.html")

@app.route("/reservar")
def reservar():
    return render_template("reservar.html")

if __name__ == '__main__': 
    app.run(debug=True)
