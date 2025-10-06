from flask import render_template, url_for

from app import app
@app.route("/reservar")
def reservar():
    return render_template("reservar.html")