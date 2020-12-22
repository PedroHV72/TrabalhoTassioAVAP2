from application.model.entity.disciplina import Disciplina
from application.model.entity.aula import Aula
from application import todas_disciplinas


class DisciplinaDAO():
    def __init__(self):
        self.todas_disciplinas = todas_disciplinas

    def retornar_todas_disciplinas(self):
        return self.todas_disciplinas

    def procurar_disciplina(self, id):
        for i in range(0, len(self.todas_disciplinas)):
            if self.todas_disciplinas[i].get_id_disciplina() == int(id):
                return self.todas_disciplinas[i]
        return None