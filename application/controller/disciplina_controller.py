from application import app
from flask import render_template, request
from application import todas_aulas
from application.model.dao.aula_DAO import AulaDAO
from application.model.dao.disciplina_DAO import DisciplinaDAO
from application.model.entity.aula import Aula


@app.route("/disciplina/<id_disciplina>")
def disciplina(id_disciplina):
    buscar = DisciplinaDAO().procurar_disciplina(id_disciplina)
    aulas_lista = buscar.get_aulas()
    return render_template("disciplina.html", aulas_lista = aulas_lista, disciplina = buscar)