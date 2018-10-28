from usuarioDAO import UsuarioDAO
import sqlite3
conexao = sqlite3.connect('organiza_com.db')
cursor = conexao.cursor()
usuarioDAO = UsuarioDAO(conexao, cursor)

class Usuario:
    def __init__(self, email, senha, nome):
        self.senha = senha
        self.nome = nome
        self.email = email

    def __str__(self):
        return ("Nome: " + self.nome + "\nEmail: " + self.email)

    def get_senha(self):
        return self.senha

    def get_nome(self):
        return self.nome

    def get_email(self):
        return self.email

    def set_senha(self, novo):
        usuarioDAO.set_senha(novo, self.email)
        self.senha = novo

    def set_nome(self, novo):
        usuarioDAO.set_nome(novo, self.email)
        self.nome = novo

    def set_email(self, novo):
        usuarioDAO.set_email(novo, self.email)
        self.email = novo

    def percorrer_tags(self):
        return usuarioDAO.percorrer_tags(self.email)

    def remover_tag(self, tag):
        usuarioDAO.remover_tag(tag, self.email)