class Aula:
    def __init__(self, id, nome, conteudo, disciplina_aula):
        self._id = id
        self._nome = nome
        self._conteudo = conteudo
        self._disciplina_aula = disciplina_aula

    def get_nomeAula(self):
        return self._nome

    def get_conteudoAula(self):
        return self._conteudo

    def get_id_aula(self):
        return self._id