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
        if len(self.atividades) != 0:
            return self.atividades
        else:
            return "\nNenhuma Atividade Cadastrada na Disciplina " + self.get_nome() + "."


    def listar_atividades_arquivadas(self):
        if len(self.arquivadas) != 0:
            return self.arquivadas
        else:
            return "\nNenhuma Atividade Arquivada na Disciplina " + self.get_nome() + "."

    def adicionar_atividade(self, atividade_adicionar):
        if len(self.atividades) == 0:
            self.atividades.append(atividade_adicionar)

        elif len(self.atividades) == 1:
            if atividade_adicionar.data_final_int < self.atividades[0].data_final_int:
                self.atividades.insert(0, atividade_adicionar)
            else:
                self.atividades.insert(1, atividade_adicionar)

        else:
            for indice in range(0, len(self.atividades) - 1):
                if atividade_adicionar.data_final_int < self.atividades[indice].data_final_int:
                    self.atividades.insert(indice, atividade_adicionar)
                    break
            if atividade_adicionar not in self.atividades:
                self.atividades.append(atividade_adicionar)



    def adicionar_atividade_arquivada(self, atividade):
        self.arquivadas.append(atividade)

    def remover_atividade(self, atividade):
        self.atividades.remove(atividade)
