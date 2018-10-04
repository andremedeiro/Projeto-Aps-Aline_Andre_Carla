class Usuario:
    def __init__(self,email, senha, nome):
        self.senha = senha
        self.nome = nome
        self.email = email
        self.disciplinas = []

    def __str__(self):
        return ("Nome: " + self.nome + "\nEmail: " + self.email)

    def get_senha(self):
        return self.senha

    def get_nome(self):
        return self.nome

    def get_email(self):
        return self.email

    def set_senha(self, novo_senha):
        self.senha = novo_senha

    def set_nome(self, novo_nome):
        self.nome = novo_nome

    def set_email(self, novo_email):
        self.email = novo_email

    def adicionar_disciplina(self, disciplina):
        self.disciplinas.append(disciplina)

    def listar_disciplinas(self):
        for disciplina in self.disciplinas:
            print(disciplina)

    def listar_atividades(self):
        for disciplina in self.disciplinas:
            disciplina.listar_atividades()
