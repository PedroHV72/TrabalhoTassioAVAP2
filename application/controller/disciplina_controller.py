from application import app
from flask import render_template, request


@app.route("/disciplina")
def disciplina():
    return render_template("disciplina.html")