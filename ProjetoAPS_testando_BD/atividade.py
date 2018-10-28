from datetime import datetime
import time
from atividadeDAO import AtividadeDAO
import sqlite3

conexao = sqlite3.connect('organiza_com.db')
cursor = conexao.cursor()

atividadeDAO = AtividadeDAO(conexao, cursor)

class Atividade:
    def __init__(self, nome, data_final,tag, conteudo, disciplina, id, situacao):
        self.nome = nome
        self.id = id
        self.data_final = data_final
        self.data_final_int = time.strptime(self.data_final, "%d/%m/%Y")
        self.conteudo = conteudo
        self.disciplina = disciplina
        self.tag = tag
        self.situacao = situacao

    def __str__(self):
        if self.situacao == 'Atividade Atrasada':
            return ('\n\033[31m' + "Nome: " + self.nome + " | ID: " + self.id + " | Disciplina: " + str(
                self.disciplina) + "\nPrazo: " + str(self.data_final) + " | " + str(self.situacao) + "\nTag: " + str(self.get_tag()) + "\n" + self.conteudo + '\033[0;0m')

        elif self.situacao == 'Atividade Concluida':
            return ('\n\033[32m' + "Nome: " + self.nome + " | ID: " + self.id + " | Disciplina: " + str(
                self.disciplina) + "\nPrazo: " + str(self.data_final) + " | " + str(self.situacao) + "\nTag: " + str(self.get_tag()) + "\n" + self.conteudo + '\033[0;0m')
        else:
            return ("\nNome: " + self.nome + " | ID: " + self.id + " | Disciplina: " + str(
                self.disciplina) + "\nPrazo: " + str(self.data_final) + " | " + str(self.situacao) + "\nTag: " + str(self.get_tag()) + "\n" + self.conteudo)

    def get_datafinal(self):
        return self.data_final

    def get_nome(self):
        return self.nome

    def get_tag(self):
        return self.tag

    def get_disciplina(self):
        return self.disciplina

    def get_id(self):
        return self.id

    def get_situacao(self):
        return self.situacao

    def set_nome(self, novo, usuario):
        atividadeDAO.set_nome(novo, self.id, usuario.get_nome(), self.disciplina)
        self.nome = novo

    def set_ID(self, novo, usuario):
        atividadeDAO.set_ID(novo, self.id, usuario.get_nome(), self.disciplina)
        self.id = novo

    def set_disciplina(self, novo, usuario):
        atividadeDAO.set_disciplina(novo, self.id, usuario.get_nome(), self.disciplina)
        self.disciplina = novo

    def set_datafinal(self, novo, usuario):
        atividadeDAO.set_datafinal(novo, self.id, usuario.get_nome(), self.disciplina)
        self.data_final = novo

    def set_situacao(self, novo, usuario):
        atividadeDAO.set_situacao(novo, self.get_id(), usuario.get_nome(), self.get_disciplina())
        self.situacao = novo

    def set_tag(self, novo, usuario):
        atividadeDAO.set_tag(novo, self.id,usuario.get_nome(), self.disciplina)
        self.tag=novo

    def set_conteudo(self, novo, usuario):
        atividadeDAO.set_conteudo(novo, self.id,usuario.get_nome(), self.disciplina)
        self.conteudo=novo

    def analisa_situacao(self):
        data_de_hoje = time.strptime(self.data(), "%d/%m/%Y")
        if self.data_final_int < data_de_hoje:
            self.situacao = "Atividade Atrasada"
        else:
            self.situacao = "Atividade no Prazo"

    def data(self):
        now = datetime.now()
        dia = now.day
        mes = now.month
        ano = now.year
        return (str(dia) + "/" + str(mes) + "/" + str(ano))

    def ajeita_data(self):
        self.data_final_int = time.strptime(self.data_final, "%d/%m/%Y")

