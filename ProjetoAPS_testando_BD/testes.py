import sqlite3
import time

conexao = sqlite3.connect('organiza_com.db')
cursor = conexao.cursor()

def criar_tabela_usuario():
    cursor.execute('CREATE TABLE IF NOT EXISTS usuario (email text primary key, senha text, nome text)')

def inserir_usuario_tabela(email, senha, nome):
    cursor.execute('INSERT INTO usuario (email, senha, nome) VALUES (?,?,?)', (email, senha, nome))
    conexao.commit()

def remover_usuario_da_tabela(email):
    cursor.execute('DELETE FROM usuario  WHERE email = ?', (email,))
    conexao.commit()

def percorrer_usuario():
    for usuario in cursor.execute('SELECT * FROM usuario'):
        print(usuario)

def buscar_usuario_na_tabela(email):
    for usuario in cursor.execute('SELECT * FROM usuario WHERE email = ?',(email,)):
        return usuario

def contar_tuplas_usuario():
    conta = 0
    for usuario in cursor.execute('select count(*) from usuario'):
        conta = usuario
    return(conta[0])

def adicionar_tag(tag, email_usuario, id_atividade):
    cursor.execute('insert into tags_usuario values(?,?,?)', (tag, email_usuario, id_atividade))
    conexao.commit()
#____________________________________________________________________
#                 FUNÇÕES SOBRE ATIVIDADE



def remover_atividade_da_tabela(id):
    cursor.execute('DELETE FROM atividade  WHERE id = ?', (id,))
    conexao.commit()

def trazer_atividade_ordenada():
    for atividade in cursor.execute('SELECT * FROM atividade ORDER BY data_final ASC'):
        print(atividade)

def adicionar_atividade(nome, id, conteudo, situacao, data_final,tag, nome_disciplina, email_usuario):
    cursor.execute('INSERT INTO atividade VALUES (?,?,?,?,?,?,?,?)',(nome, id, conteudo, situacao, data_final,tag, nome_disciplina, email_usuario))
    conexao.commit()

def percorrer_atividade():
    for atividade in cursor.execute('SELECT * FROM atividade'):
        print(atividade)

def contar_tuplas_atividade():
    conta = 0
    for atividade in cursor.execute('select count(*) from atividade'):
        conta = atividade
    return(conta[0])

#________________________________________________________________________
#             FUNÇÕES SOBRE DISCIPLINA


def contar_tuplas_disciplina():
    conta = 0
    for disciplina in cursor.execute('select count(*) from disciplina'):
        conta = disciplina
    return(conta[0])

def percorrer_disciplina():
    for disciplina in cursor.execute('SELECT * FROM disciplina'):
        print(disciplina)

def adicionar_disciplina(nome, professor, email_usuario):
    cursor.execute('INSERT INTO disciplina VALUES (?,?,?)', (nome, professor, email_usuario))
    conexao.commit()





#-------------------------------------------------------------------

class Usuario:
    def __init__(self, email, senha, nome):
        self.nome = nome
        self.email = email
        self.senha = senha

    def __str__(self):
        return ("Nome: " + self.nome + "\nEmail: " + self.email)

    def get_nome(self):
        return self.nome

    def get_email(self):
        return self.email

    def get_senha(self):
        return self.senha

    def set_nome(self, novo):
        self.nome = novo

    def set_matricula(self, novo):
        self.email = novo

    def set_senha(self, novo):
        self.senha = novo


def cadastrar_usuario(email, senha, nome):
    busca = buscar_usuario_na_tabela(email)
    if busca == None:
        inserir_usuario_tabela(email, senha, nome)
        print("usuario Cadastrado com Sucesso")
    else:
        print("usuario com tal email já existe")

def logar(email, senha):
    usuario = trazer_usuario(email)
    if usuario != None:
        if senha == usuario.get_senha():
            print("Logado com Sucesso")

        else:
            print("Senha Incorreta")
    else:
        print("Não foi encontrado nenhum usuario com este email")

def trazer_usuario(email):
    usuario = buscar_usuario_na_tabela(email)
    if usuario != None:
        return Usuario(usuario[0], usuario[1], usuario[2])





#--------------------------------------------------












