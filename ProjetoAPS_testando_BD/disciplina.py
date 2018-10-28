from disciplinaDAO import DisciplinaDAO
import sqlite3
conexao = sqlite3.connect('organiza_com.db')
cursor = conexao.cursor()
disciplinaDAO = DisciplinaDAO(conexao, cursor)

class Disciplina:
    def __init__(self, nome, professor):
        self.nome = nome
        self.professor = professor

    def __str__(self):
        return ("Nome: " + self.nome + "\nProfessor: " + self.professor)

    def get_nome(self):
        return self.nome

    def get_professor(self):
        return self.professor

    def set_nome(self, novo, nome_usuario, nome_disciplina):
        disciplinaDAO.set_nome(novo, nome_usuario, nome_disciplina)
        self.nome = novo

    def set_professor(self, novo, nome_usuario, nome_disciplina):
        disciplinaDAO.set_professor(novo, nome_usuario, nome_disciplina)
        self.professor = novo
