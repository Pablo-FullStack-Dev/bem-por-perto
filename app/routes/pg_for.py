from flask import render_template, url_for

from app import app
@app.route("/ajuda")
def ajuda():
    return render_template("ajuda.html")