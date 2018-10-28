


def mudar_cor(texto, cor):
    return str('\033[' + str(cor) + 'm' + str(texto) + '\033[0;0m')

class UsuarioDAO:

    def __init__(self, conexao, cursor):
        self.conexao = conexao
        self.cursor = cursor

    def criar_tabela_usuario(self):
        self.cursor.execute('CREATE TABLE IF NOT EXISTS usuario (email text primary key, senha text, nome text)')

    def inserir_usuario_tabela(self,email, senha, nome):
        self.cursor.execute('INSERT INTO usuario (email, senha, nome) VALUES (?,?,?)', (email, senha, nome))
        self.conexao.commit()

    def remover_usuario_da_tabela(self,email):
        self.cursor.execute('DELETE FROM usuario  WHERE email = ?', (email,))
        self.conexao.commit()

    def percorrer_usuario(self):
        for usuario in self.cursor.execute('SELECT * FROM usuario'):
            print('')
            print(mudar_cor(self.tranformar_tupla(usuario), 34))

    def buscar_usuario_na_tabela(self,email):
        for usuario in self.cursor.execute('SELECT * FROM usuario WHERE email = ?',(email,)):
            return usuario

    def contar_tuplas_usuario(self):
        conta = 0
        for usuario in self.cursor.execute('select count(*) from usuario'):
            conta = usuario
        return(conta[0])

    def adicionar_tag(self,tag, email_usuario, id_atividade):
        self.cursor.execute('insert into tags_usuario values(?,?,?)', (tag, email_usuario, id_atividade))
        self.conexao.commit()

    def tranformar_tupla(self, tupla):
        from usuario import Usuario
        return Usuario(tupla[0], tupla[1], tupla[2])

    def contar_tags(self, email_usuario):
        conta = 0
        for tag in self.cursor.execute('select count(*) from tags_usuario where email_usuario = ?',(email_usuario,)):
            conta = tag
        return (conta[0])

    def set_nome(self, novo, email_usuario):
        self.cursor.execute('update usuario set nome = ? where email = ?',(novo, email_usuario))
        self.conexao.commit()

    def set_senha(self, novo, email_usuario):
        self.cursor.execute('update usuario set senha = ? where email = ?', (novo, email_usuario))
        self.conexao.commit()

    def set_email(self, novo, email_usuario):
        self.cursor.execute('update usuario set email = ? where email = ?', (novo, email_usuario))
        self.conexao.commit()

    def percorrer_tags(self, email_usuario):
        for tag in self.cursor.execute('select distinct tag from tags_usuario where email_usuario = ?', (email_usuario,)):
            return tag

    def remover_tag(self, tag, email_usuario):
        self.cursor.execute('delete from tags_usuario where email_usuario = ? and tag = ?',(email_usuario, tag))
        self.conexao.commit()
