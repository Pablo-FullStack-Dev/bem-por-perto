from flask import render_template, url_for

from app import app



@app.route("/login")
def login():
    return render_template("login.html")