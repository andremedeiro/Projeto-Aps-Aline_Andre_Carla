from datetime import datetime
import time


class Atividade:
    def __init__(self, nome, data_final, conteudo, disciplina, tags, id):
        self.nome = nome
        self.id = id
        self.data_final = data_final
        self.conteudo = conteudo
        self.disciplina = disciplina
        self.tags = tags
        self.situacao = self.analisa_situacao()

    def __str__(self):
        if self.situacao == 'Atividade Atrasada':
            return ('\033[31m' + "Nome: " + self.nome + " | ID: " + self.id + " | Disciplina: " + str(
                self.disciplina.nome) + "\nPrazo: " + self.data_final + " | " + str(self.situacao) + "\nTags: " + str(
                self.tags) + "\n" + self.conteudo + '\033[0;0m')

        elif self.situacao == 'Atividade Concluida':
            return ('\033[32m' + "Nome: " + self.nome + " | ID: " + self.id + " | Disciplina: " + str(
                self.disciplina.nome) + "\nPrazo: " + self.data_final + " | " + str(self.situacao) + "\nTags: " + str(
                self.tags) + "\n" + self.conteudo + '\033[0;0m')
        else:
            return ("Nome: " + self.nome + " | ID: " + self.id + " | Disciplina: " + str(
                self.disciplina.nome) + "\nPrazo: " + self.data_final + " | " + str(self.situacao) + "\nTags: " + str(
                self.tags) + "\n" + self.conteudo)

    def get_datafinal(self):
        return self.data_final

    def get_nome(self):
        return self.nome

    def get_tags(self):
        return self.tags

    def get_disciplina(self):
        return self.disciplina

    def get_id(self):
        return self.id

    def set_nome(self, novo_nome):
        self.nome = novo_nome

    def set_ID(self, novo):
        self.id = novo

    def set_disciplina(self, novo):
        self.disciplina = novo

    def set_datafinal(self, novo):
        self.data_final = novo

    def set_situacao(self, nova_situacao):
        self.situacao = nova_situacao

    def set_conteudo(self, novo):
        self.conteudo = novo

    def set_tags(self, novo):
        self.tags = novo

    def analisa_situacao(self):
        data_de_hoje = time.strptime(self.data(), "%d/%m/%Y")
        data_final = time.strptime(self.data_final, "%d/%m/%Y")
        if data_final < data_de_hoje:
            return ("Atividade Atrasada")

        else:
            return ("Atividade no Prazo")

    def data(self):
        now = datetime.now()
        dia = now.day
        mes = now.month
        ano = now.year
        return (str(dia) + "/" + str(mes) + "/" + str(ano))