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

    def get_disciplina(self):
        return len(self.disciplinas)

    def set_senha(self, novo_senha):
        self.senha = novo_senha

    def set_nome(self, novo_nome):
        self.nome = novo_nome

    def set_email(self, novo_email):
        self.email = novo_email

    def adicionar_disciplina(self, disciplina):
        self.disciplinas.append(disciplina)

    def listar_disciplinas(self):
        from sistema import Sistema
        sistema=Sistema()
        print(sistema.mudar_cor("Disciplinas:", 34))
        for disciplina in self.disciplinas:
            print(" ")
            print(sistema.mudar_cor(disciplina,34))

    def listar_atividades(self):
        from sistema import Sistema
        sistema = Sistema()
        atividades = []
        for disciplina in self.disciplinas:
            atividades.append(disciplina.listar_atividades())
        if len(atividades) == 0:
            print(sistema.mudar_cor("Nenhuma Atividade Cadastrada", 31))
        else:
            for lista in atividades:
                if isinstance(lista, str) == False:
                    for atividade in lista:
                        print("\n"+str(atividade))
                else:
                    print(sistema.mudar_cor(lista, 34))


    def listar_atividades_arquivadas(self):
        from sistema import Sistema
        sistema = Sistema()
        atividades = []
        for disciplina in self.disciplinas:
            atividades.append(disciplina.listar_atividades_arquivadas())
        if len(atividades) == 0:
            print(sistema.mudar_cor("Nenhuma Atividade Arquivada", 31))
        else:
            for lista in atividades:
                if isinstance(lista, str) == False:
                    for atividade in lista:
                        print("\n" + str(atividade))
                else:
                    print(sistema.mudar_cor(lista, 34))

    def adicionar_tag(self, tag):
        self.tags_personalizadas.append(tag)

    def remover_tag(self, tag):
        if tag in self.tags_personalizadas:
            self.tags_personalizadas.remove(tag)
            for disciplina in self.disciplinas:
                for atividade in disciplina.atividades:
                    atividade.tags.remove(tag)
        else:
            print("A Tag "+tag+ " Não foi Criada")