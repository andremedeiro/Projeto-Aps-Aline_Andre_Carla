class Disciplina:
    def __init__(self, nome, professor):
        self.nome = nome
        self.professor = professor
        self.atividades = []
        self.arquivadas = []

    def __str__(self):
        return ("Nome: " + self.nome + "\nProfessor: " + self.professor)

    def get_nome(self):
        return self.nome

    def get_professor(self):
        return self.professor

    def set_nome(self, novo_nome):
        self.nome = novo_nome

    def set_professor(self, novo):
        self.professor = novo

    def listar_atividades(self):
        if len(self.atividades) == 0:
            return None
        else:
            for atividade in self.atividades:
                print("")
                print(atividade)

    def listar_atividades_arquivadas(self):
        if len(self.arquivadas) == 0:
            return None
        else:
            for atividade in self.arquivadas:
                print("")
                print(atividade)

    def adicionar_atividade(self, atividade):
        self.atividades.append(atividade)

    def adicionar_atividade_arquivada(self, atividade):
        self.arquivadas.append(atividade)

    def remover_atividade(self, atividade):
        self.atividades.remove(atividade)
