class Disciplina:
    def __init__(self, id, nome, professor, periodo, aulas):
        self._id = id
        self._nome = nome
        self._professor = professor
        self._periodo = periodo
        self._aulas = aulas

    def get_id_disciplina(self):
        return self._id

    def get_nome_disciplina(self):
        return self._nome

    def get_professor(self):
        return self._professor

    def get_periodo(self):
        return self._periodo

    def get_aulas(self):
        return self._aulas