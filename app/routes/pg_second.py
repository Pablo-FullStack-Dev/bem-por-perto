from flask import render_template, url_for
from app import app

@app.route("/sobre")
def sobre():
    return render_template("sobre.html")