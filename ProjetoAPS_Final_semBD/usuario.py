class Usuario:
    def __init__(self, email, senha, nome):
        self.senha = senha
        self.nome = nome
        self.email = email
        self.disciplinas = []
        self.tags_personalizadas = []


    def __str__(self):
        return ("Nome: " + self.nome + "\nEmail: " + self.email)

    def get_senha(self):
        return self.senha

    def get_nome(self):
        return self.nome

    def get_email(self):
        return self.email

    def get_tags_personalizdas(self):
        return self.tags_personalizadas

    def set_senha(self, novo_senha):
        self.senha = novo_senha

    def set_nome(self, novo_nome):
        self.nome = novo_nome

    def set_email(self, novo_email):
        self.email = novo_email

    def adicionar_disciplina(self, disciplina):
        self.disciplinas.append(disciplina)

    def listar_disciplinas(self):
        if len(self.disciplinas) == 0:
            return None
        else:
            for disciplina in self.disciplinas:
                print(" ")
                print(disciplina)

    def listar_atividades(self):
        for disciplina in self.disciplinas:
            disciplina.listar_atividades()

    def listar_atividades_arquivadas(self):
        for disciplina in self.disciplinas:
            disciplina.listar_atividades_arquivadas()

    def adicionar_tag(self, tag):
        self.tags_personalizadas.append(tag)

    def remover_tag(self, tag):
        if tag in self.tags_personalizadas:
            self.tags_personalizadas.remove(tag)
            for disciplina in self.disciplinas:
                for atividade in disciplina.atividades:
                    atividade.tags.remove(tag)
        else:
            print("Esta Tag Não foi Criada")