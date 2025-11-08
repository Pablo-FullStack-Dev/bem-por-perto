from flask import render_template
from app import app
from config import dados

@app.route("/")
def home():
    return render_template("index.html", dados=dados)