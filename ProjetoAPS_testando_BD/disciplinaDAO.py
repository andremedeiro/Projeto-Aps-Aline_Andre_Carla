def mudar_cor(texto, cor):
    return str('\033[' + str(cor) + 'm' + str(texto) + '\033[0;0m')

class DisciplinaDAO:

    def __init__(self, conexao, cursor):
        self.conexao = conexao
        self.cursor = cursor

    def contar_tuplas_disciplina(self, email_usuario):
        conta = 0
        for disciplina in self.cursor.execute('select count(*) from disciplina where email_usuario = ?',(email_usuario,)):
            conta = disciplina
        return (conta[0])

    def percorrer_disciplina(self, email_usuario):
        for disciplina in self.cursor.execute('SELECT * FROM disciplina where email_usuario = ?', (email_usuario,)):
            print(mudar_cor("\n"+str(self.transforma_disciplina(disciplina)), 34))

    def adicionar_disciplina(self, nome, professor, email_usuario):
        self.cursor.execute('INSERT INTO disciplina VALUES (?,?,?)', (nome, professor, email_usuario))
        self.conexao.commit()

    def buscar_disciplina(self, nome, email_usuario):
        for tupla in self.cursor.execute('select * from disciplina where email_usuario = ?', (email_usuario,)):
            if nome == tupla[0]:
                return self.transforma_disciplina(tupla)

    def transforma_disciplina(self, tupla):
        if tupla != None:
            from disciplina import Disciplina
            return Disciplina(tupla[0], tupla[1])

    def set_nome(self, novo, email_usuario, disciplina):
        self.cursor.execute('update disciplina set nome = ? where email_usuario = ? and nome = ?', (novo, email_usuario,disciplina))
        self.conexao.commit()

    def set_professor(self, novo, email_usuario, disciplina):
        self.cursor.execute('update disciplina set professor = ? where email_usuario = ? and nome = ?', (novo, email_usuario, disciplina))
        self.conexao.commit()

    def set_usuario(self, novo, email_usuario):
        self.cursor.execute('update disciplina set email_usuario = ? where email_usuario = ?',(novo, email_usuario))
        self.conexao.commit()


