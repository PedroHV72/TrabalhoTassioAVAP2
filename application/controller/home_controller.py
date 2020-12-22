from application import app
from flask import render_template, request
from application.model.entity.disciplina import Disciplina
from application.model.dao.disciplina_DAO import DisciplinaDAO
from application import todas_disciplinas


@app.route("/")
def hello():
    lista_disciplinas = todas_disciplinas
    return render_template("index.html", todas_disciplinas = todas_disciplinas)