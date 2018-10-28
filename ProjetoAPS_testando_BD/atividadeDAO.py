

class AtividadeDAO:

    def __init__(self, conexao, cursor):
        self.conexao = conexao
        self.cursor = cursor

    def trazer_atividade_ordenada(self, email_usuario):
        for atividade in self.cursor.execute('SELECT * FROM atividade where email_usuario = ? ORDER BY data_final ASC', (email_usuario, )):
            if atividade[3] != "Atividade Concluida":
                print(self.transforma_atividade(atividade))

    def listar_atividades_arquivadas(self, email_usuario):
        for atividade in self.cursor.execute('SELECT * FROM atividade where email_usuario = ? and situacao = "Atividade Concluida"',(email_usuario,)):
            print(self.transforma_atividade(atividade))

    def adicionar_atividade(self,nome, id, conteudo, situacao, data_final,tag, nome_disciplina, email_usuario):
        self.cursor.execute('INSERT INTO atividade VALUES (?,?,?,?,?,?,?,?)',(nome, id, conteudo, situacao, data_final,tag, nome_disciplina, email_usuario))
        self.conexao.commit()


    def contar_tuplas_atividade(self, email_usuario):
        conta = 0
        for atividade in self.cursor.execute('select count(*) from atividade where email_usuario = ? and situacao != "Atividade Concluida"',(email_usuario,)):

            conta = atividade
        return(conta[0])

    def contar_atividades_arquivadas(self, email_usuario):
        conta = 0
        for atividade in self.cursor.execute('select count(*) from atividade where email_usuario = ? and situacao = "Atividade Concluida"',(email_usuario,)):
            conta = atividade
        return(conta[0])

    def buscar_atividade(self, id, email_usuario, nome_disciplina):
        for tupla in self.cursor.execute('select * from atividade where email_usuario = ? and nome_disciplina = ?', (email_usuario, nome_disciplina)):
            if id == tupla[1]:
                return self.transforma_atividade(tupla)

    def transforma_atividade(self, tupla):
        from atividade import Atividade
        atividade = Atividade(tupla[0], tupla[4],tupla[5], tupla[2], tupla[6], tupla[1],tupla[3])
        if atividade.get_situacao() != 'Atividade Concluida':
            atividade.analisa_situacao()
        return atividade

    def remover_atividade(self, id, email_usuario, nome_disciplina):
        self.cursor.execute('delete from atividade where id = ? and email_usuario = ? and nome_disciplina = ?', (id, email_usuario, nome_disciplina))
        self.conexao.commit()

    def set_tag(self, novo, id, email_usuario, nome_disciplina):
        self.cursor.execute('update atividade set tag = ? where id = ? and email_usuario = ? and nome_disciplina = ?', (novo, id, email_usuario, nome_disciplina))
        self.conexao.commit()

    def set_situacao(self, novo, id, email_usuario, nome_disciplina):
        self.cursor.execute('update atividade set situacao = ? where id = ? and email_usuario = ? and nome_disciplina = ?',(novo, id, email_usuario, nome_disciplina))
        self.conexao.commit()

    def set_conteudo(self, novo, id, email_usuario, nome_disciplina):
        self.cursor.execute('update atividade set conteudo = ? where id = ? and email_usuario = ? and nome_disciplina = ?',(novo, id, email_usuario, nome_disciplina))
        self.conexao.commit()

    def set_ID(self, novo, id, email_usuario, nome_disciplina):
        self.cursor.execute('update atividade set id = ? where id = ? and email_usuario = ? and nome_disciplina = ?',(novo, id, email_usuario, nome_disciplina))
        self.conexao.commit()

    def set_nome(self, novo, id, email_usuario, nome_disciplina):
        self.cursor.execute('update atividade set nome = ? where id = ? and email_usuario = ? and nome_disciplina = ?',(novo, id, email_usuario, nome_disciplina))
        self.conexao.commit()

    def set_datafinal(self, novo, id, email_usuario, nome_disciplina):
        self.cursor.execute('update atividade set data_final = ? where id = ? and email_usuario = ? and nome_disciplina = ?',(novo, id, email_usuario, nome_disciplina))
        self.conexao.commit()

    def set_disciplina(self, novo, id, email_usuario, nome_disciplina):
        self.cursor.execute('update atividade set nome_disciplina = ? where id = ? and email_usuario = ? and nome_disciplina = ?',(novo, id, email_usuario, nome_disciplina))
        self.conexao.commit()

    def set_usuario(self, novo, email_usuario):
        self.cursor.execute('update atividade set email_usuario = ? where email_usuario = ?',(novo, email_usuario))
        self.conexao.commit()

    def set_disciplina_total(self, novo, nome_disciplina, email_usuario):
        self.cursor.execute('update atividade set nome_disciplina = ? where email_usuario = ? and nome_disciplina = ?',(novo, email_usuario, nome_disciplina))

    def excluir_tag(self, tag, email_usuario):
        self.cursor.execute('update atividade set tag = "None" where email_usuario = ? and tag = ?',(email_usuario, tag))


