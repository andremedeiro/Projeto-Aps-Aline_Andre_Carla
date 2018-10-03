class Disciplina:
    def __init__(self, nome, professor):
        self.nome = nome
        self.professor = professor
        self.atividades = []

    def __str__(self):
        return ("Nome: " + self.nome + "\nProfessor: " + self.professor)

    def get_nome(self):
        return self.nome

    def get_profissao(self):
        return self.profissao

    def set_nome(self, novo_nome):
        self.nome = novo_nome

    def listar_atividades(self):
        for atividade in self.atividades:
            print(" ")
            print(atividade)

    def adicionar_atividade(self, atividade):
        self.atividades.append(atividade)
