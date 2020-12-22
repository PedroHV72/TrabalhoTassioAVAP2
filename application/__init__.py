from flask import Flask
import os
from application.model.entity.aula import Aula
from application.model.entity.disciplina import Disciplina


app = Flask(__name__, static_folder=os.path.abspath("application/view/static"), template_folder=os.path.abspath("application/view/templates"))


aula1 = Aula(1, "Aula 1", "Introdução ao Linux", "Sistemas Operacionais")
aula2 = Aula(2, "Aula 1", "Introdução ao grid layout e flexbox", "Interface com Usuário")
aula3 = Aula(3, "Aula 2", "Introdução ao Windows", "Sistemas Operacionais")
aula4 = Aula(4, "Aula 2", "Práticas com CSS 3", "Interface com Usuário")
todas_aulas = [aula1, aula2, aula3, aula4]

disciplina1 = Disciplina(1, "Sistemas Operacionais", "Felipe Melo", 4, [aula1, aula3])
disciplina2 = Disciplina(2, "Interface com Usuário", "Tássio Auad", 4, [aula2, aula4])
todas_disciplinas = [disciplina1, disciplina2]

from application.controller import home_controller
from application.controller import disciplina_controller