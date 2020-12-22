from application.model.entity.disciplina import Disciplina
from application.model.entity.aula import Aula
from application import todas_aulas


class AulaDAO():
    def __init__(self):
        self.todas_aulas = todas_aulas

    def retornar_todas_aulas(self):
        return self.todas_aulas

    def procurar_aula(self, id):
        for i in range(0, len(self._todas_aulas)):
            if self._todas_aulas[i].get_id() == int(id):
                return self._todas_aulas[i]
        return None