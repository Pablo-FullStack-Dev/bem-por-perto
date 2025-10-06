from flask import render_template, url_for
from app import app

@app.route("/explorar")
def explorar():
    return render_template("explorar.html")