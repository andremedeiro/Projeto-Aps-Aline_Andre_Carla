
from usuarioDAO import UsuarioDAO
from atividadeDAO import AtividadeDAO
from disciplinaDAO import DisciplinaDAO
import time

import sqlite3

conexao = sqlite3.connect('organiza_com.db')
cursor = conexao.cursor()

usuarioDAO = UsuarioDAO(conexao, cursor)
atividadeDAO = AtividadeDAO(conexao, cursor)
disciplinaDAO = DisciplinaDAO(conexao, cursor)



def mudar_cor(texto, cor):
    return str('\033[' + str(cor) + 'm' + str(texto) + '\033[0;0m')


class Sistema:
    def __init__(self):
        self.tags_programadas = ["projeto","prova", "mini-teste", "monitoria", "seminario"]

    # ______________________________________________________________________
    #  METODOS SOBRE USUARIO
    def cadastrar_usuario(self, email, senha, nome):
        usuarioDAO.inserir_usuario_tabela(email, senha, nome)

    def remover_usuario(self, usuario):
        usuarioDAO.remover_usuario_da_tabela(usuario.get_email())

    def listar_usuarios(self):
        if usuarioDAO.contar_tuplas_usuario() == 0:
            print(mudar_cor("Nenhum Usuario Cadastrado", 31))
        else:
            print(mudar_cor("\nUSUARIOS:", 34))
            usuarioDAO.percorrer_usuario()

    def buscar_usuario(self, email):
        tupla = usuarioDAO.buscar_usuario_na_tabela(email)
        if tupla != None:
            return usuarioDAO.tranformar_tupla(tupla)

    def logar(self, email, senha):
        if usuarioDAO.contar_tuplas_usuario() == 0:
            print(mudar_cor("Nenhum Usuario Cadastrado", 31))
        else:
            usuario = self.buscar_usuario(email)
            if usuario != None:
                if senha == usuario.get_senha():
                    print(mudar_cor("Logado Com Sucesso", 32))
                    opcao2 = ''
                    while opcao2 != 'x':
                            opcao2 = self.menu_logado(usuario)
                else:
                    print(mudar_cor("Senha Incorreta", 31))
            else:
                print(mudar_cor("Não foi encontrado nenhum usuario com este email", 31))

    # _________________________________________________________________________
    #     METODOS SOBRE ATIVIDADE

    def adicionar_tag(self, tag, atividade, usuario):
        if tag in self.tags_programadas:
            atividade.set_tag(tag, usuario)
        else:
            usuarioDAO.adicionar_tag(tag, usuario.get_email(), atividade.get_id())
            atividade.set_tag(tag, usuario)

    def criar_atividade(self, nome, data_final,tag,conteudo, nome_disciplina, id, usuario):
        atividadeDAO.adicionar_atividade(nome, id, conteudo,'', data_final,tag, nome_disciplina, usuario.get_email())

    def listar_atividades(self, usuario):
        if atividadeDAO.contar_tuplas_atividade(usuario.get_email()) == 0:
            print(mudar_cor("\nNenhuma Atividade Cadastrada",31))
        else:
            print(mudar_cor("\nATIVIDADES:", 34))
            print(atividadeDAO.trazer_atividade_ordenada(usuario.get_email()))

    def buscar_atividade(self, id, usuario, nome_disciplina):
        atividade = atividadeDAO.buscar_atividade(id, usuario.get_email(), nome_disciplina)
        if atividade != None:
            return atividade

    def listar_atividades_arquivadas(self, email_usuario):
        if atividadeDAO.contar_atividades_arquivadas(email_usuario) != 0:
            print(mudar_cor('\nATIVIDADES ARQUIVADAS: ',32))
            atividadeDAO.listar_atividades_arquivadas(email_usuario)
        else:
            print(mudar_cor("Nenhuma Atividade Arquivada", 31))

    def remover_atividade(self, atividade, usuario):
        atividadeDAO.remover_atividade(atividade.get_id(), usuario.get_email(), atividade.get_disciplina())

    def concluir_atividade(self, atividade, usuario):
        atividade.set_situacao("Atividade Concluida", usuario)

    # __________________________________________________________________________________
    #      METODOS SOBRE DISCIPLINA

    def buscar_disciplina(self, nome, usuario):
        return disciplinaDAO.buscar_disciplina(nome, usuario.get_email())

    def criar_disciplina(self, nome, professor, usuario):
        disciplinaDAO.adicionar_disciplina(nome, professor, usuario.get_email())

    def listar_disciplinas(self, usuario):
        if disciplinaDAO.contar_tuplas_disciplina(usuario.get_email()) == 0:
            print(mudar_cor("Não foi cadastrada nenhuma disciplina", 31))
        else:
            print(mudar_cor("\nDISCIPLINAS:", 34))
            disciplinaDAO.percorrer_disciplina(usuario.get_email())

    # ___________________________________________________________________________________
    #                        MENUS
    def menu(self):
        print("----------------- HOME INCIAL -------------------")
        print("1 - Cadastrar Usuario")
        print("2 - Listar Usuarios")
        print("3 - Logar")
        print('x - Sair')
        opcao = input("Digite a opção desejada: ")

        if opcao == '1':
            email = str(input("\nEmail: "))
            usuario = self.buscar_usuario(email)
            if usuario == None:
                senha = str(input("Senha: "))
                nome = str(input("Nome: "))
                self.cadastrar_usuario(email, senha, nome)
            else:
                print(mudar_cor("Úsuario Já Existe", 31))

        elif opcao == '2':
            self.listar_usuarios()

        elif opcao == '3':
            print("\nLogar")
            email = str(input("Email: "))
            senha = str(input("Senha: "))
            self.logar(email, senha)
        elif opcao != 'x':
            print(mudar_cor("\nOpção Não Valida", 31))
        return opcao

    def menu_logado(self, usuario):
        print("")
        print("------------------- SEU PERFIL --------------------")
        time.sleep(1)
        self.listar_atividades(usuario)
        print("")
        print("1 - Remover Conta")
        print("2 - Criar Disciplina")
        print("3 - Listar Disciplinas")
        print("4 - Criar Atividade")
        print("5 - Listar Atividades Arquivadas")
        print("6 - Concluir Atividade")
        print("7 - Editar Informações(Excluir Tags do Usuario)")
        print('x - Sair')
        opcao2 = input("Digite a opção desejada: ")

        if opcao2 == '1':
            self.remover_usuario(usuario)
            opcao2 = 'x'

        elif opcao2 == '2':
            nome = input("Nome da Disciplina: ")
            disciplina = self.buscar_disciplina(nome, usuario)
            if disciplina == None:
                professor = input("Professor da Disciplina: ")
                self.criar_disciplina(nome, professor, usuario)
            else:
                print(mudar_cor("Disciplina Já Existe", 31))

        elif opcao2 == '3':
                self.listar_disciplinas(usuario)

        elif opcao2 == '4':
            disciplina = input("De qual Disciplina é esta Atividade? ")
            disciplina = self.buscar_disciplina(disciplina, usuario)
            if disciplina != None:
                nome = input("Nome da Atividade: ")
                id = input("Informe um número para identifica-la: ")
                if self.buscar_atividade(id, usuario, disciplina.get_nome()) == None:
                    data_final = input("Prazo da atividade(DD/MM/AAAA): ")
                    conteudo = input('Conteudo: ')
                    tag = input("Tag: ")
                    if tag in self.tags_programadas:
                        self.criar_atividade(nome, data_final, tag, conteudo, disciplina.get_nome(), id, usuario)
                        atividade = self.buscar_atividade(id, usuario, disciplina.get_nome())
                        self.adicionar_tag(tag, atividade, usuario)
                    else:
                        if usuarioDAO.contar_tags(usuario.get_email()) < 50:
                            self.criar_atividade(nome, data_final, tag, conteudo, disciplina.get_nome(), id, usuario)
                            atividade = self.buscar_atividade(id, usuario, disciplina.get_nome())
                            self.adicionar_tag(tag, atividade, usuario)
                        else:
                            print(mudar_cor("Não foi possivel adicionar esta tag,\nHá 50 tags personalizadas criadas em seu Usuario,\n Você pode excluir algumas na opção de editar informações", 31))
                            self.criar_atividade(nome, data_final, None, conteudo, disciplina.get_nome(), id, usuario)
                else:
                    print(mudar_cor("ID já Existe", 31))

            else:
                print(mudar_cor("Disciplina Não Existe", 31))

        elif opcao2 == '5':
            self.listar_atividades_arquivadas(usuario.get_email())

        elif opcao2 == '6':
            disciplina = input("De qual disciplina é a atividade? ")
            disciplina = self.buscar_disciplina(disciplina, usuario)
            if disciplina != None:
                id = input("Informe o ID da Atividade: ")
                atividade = self.buscar_atividade(id, usuario, disciplina.get_nome())
                if atividade != None:
                    atitude = input('Atividade foi concluida, deseja exclui-la? [sim/nao] ')
                    if atitude == "sim":
                        self.remover_atividade(atividade, usuario)
                        print(mudar_cor("A Atividade " + str(atividade.get_nome()) + " Foi Excluida com Sucesso", 32))

                    else:
                        self.concluir_atividade(atividade, usuario)
                        print(mudar_cor("A Atividade " + str(atividade.get_nome()) + " Foi Arquivada e Concluida com Sucesso", 32))

                else:
                    print(mudar_cor("Atividade Não Existe", 31))
            else:
                print(mudar_cor("Esta Disciplina Não Existe", 31))

        elif opcao2 == '7':
            print(" ")
            print("1 - Editar Usuario(Excluir Tags)")
            print("2 - Editar Disciplina")
            print("3 - Editar Atividade")
            print("  ")
            opcao4 = input("Digite o número para qual atributo deseja alterar: ")
            print("  ")

            if opcao4 == '1':
                print("1 - Alterar Nome")
                print("2 - Alterar Email")
                print("3 - Alterar Senha")
                print("4 - Excluir Tags Personalizadas")
                print("  ")
                opcao3 = input("Digite o número para qual atributo deseja alterar: ")
                print("  ")

                if opcao3 == '1':
                    novo = input("Digite o novo nome: ")
                    usuario.set_nome(novo)

                elif opcao3 == '2':
                    novo = input("Digite o novo email: ")
                    teste = self.buscar_usuario(novo)
                    if teste == None:
                        disciplinaDAO.set_usuario(novo, usuario.get_email())
                        atividadeDAO.set_usuario(novo, usuario.get_email())
                        usuario.set_email(novo)


                    else:
                        print(mudar_cor("Email em Uso", 31))

                elif opcao3 == '3':
                    novo = input("Digite a nova Senha: ")
                    confirmar = input("Confirme a Senha Digitada: ")
                    if novo == confirmar:
                        usuario.set_senha(novo)
                    else:
                        print(mudar_cor("Senhas Não Coincidem", 31))

                elif opcao3 == '4':
                    if usuarioDAO.contar_tags(usuario.get_email()) != 0:
                        print(usuario.percorrer_tags())
                        excluir=input("Essas são as tags Criadas por você,\n informe as tags que deseja excluir separando-as por virgula: ").split(",")
                        for tag in excluir:
                            usuario.remover_tag(tag)
                            atividadeDAO.excluir_tag(tag, usuario.get_email())
                    else:
                        print(mudar_cor("Não Existem Tags Personalizadas", 31))

                else:
                    print(mudar_cor("\nOpção Não Valida", 31))

            elif opcao4 == '2':
                Nome = input("Nome da Disciplina que Deseja Editar: ")
                disciplina = self.buscar_disciplina(Nome, usuario)
                if disciplina != None:
                    print("1 - Alterar Nome")
                    print("2 - Alterar Professor")
                    print(" ")
                    opcao3 = input("Digite o número para qual atributo deseja alterar: ")
                    print("  ")

                    if opcao3 == '1':
                        novo = input("Digite o novo nome: ")
                        teste = self.buscar_disciplina(novo, usuario)
                        if teste == None:
                            atividadeDAO.set_disciplina_total(novo, disciplina.get_nome(), usuario.get_email())
                            disciplina.set_nome(novo, usuario.get_email(), disciplina.get_nome())
                        else:
                            print(mudar_cor('Este Nome de disciplina já esta em uso', 31))

                    elif opcao3 == '2':
                        novo = input("Digite o novo Professor: ")
                        disciplina.set_professor(novo, usuario.get_email(), disciplina.get_nome())
                else:
                    print(mudar_cor("Disciplina Não Existe", 31))


            elif opcao4 == '3':
                disciplina = input("De qual disciplina é a atividade? ")
                disciplina = self.buscar_disciplina(disciplina, usuario)
                if disciplina != None:
                    ID = input("ID da Atividade que Deseja Editar: ")
                    atividade = self.buscar_atividade(ID, usuario, disciplina.get_nome())
                    if atividade != None:
                        print("1 - Alterar Nome")
                        print("2 - Alterar ID")
                        print("3 - Alterar Disciplina")
                        print("4 - Alterar Data Final")
                        print("5 - Alterar Tag")
                        print("6 - Alterar Conteudo")

                        opcao3 = input("Digite o número para qual atributo deseja alterar: ")
                        print("  ")

                        if opcao3 == '1':
                            novo = input("Digite o novo nome: ")
                            atividade.set_nome(novo, usuario)

                        if opcao3 == '2':
                            novo = input("Novo ID: ")
                            teste = self.buscar_atividade(novo, usuario, disciplina.get_nome())
                            if teste == None:
                                atividade.set_ID(novo, usuario)
                            else:
                                print(mudar_cor("ID em Uso", 31))

                        if opcao3 == '3':
                            novo = input("Nova Disciplina: ")
                            disciplina_destino = self.buscar_disciplina(novo, usuario)
                            if disciplina_destino != None:
                                atividade.set_disciplina(disciplina_destino.get_nome(), usuario)
                            else:
                                print(mudar_cor("Disciplina Não Existe", 31))

                        if opcao3 == '4':
                            novo = input("Novo Prazo (DD/MM/AAAA): ")
                            atividade.set_datafinal(novo, usuario)
                            atividade.ajeita_data()
                            atividade.analisa_situacao()

                        if opcao3 == '5':
                            tag = input("Tag: ")
                            if tag in self.tags_programadas:
                                self.adicionar_tag(tag, atividade, usuario)
                            else:
                                if usuarioDAO.contar_tags(usuario.get_email()) > 50:
                                    print(mudar_cor(
                                        "Não foi possivel adicionar esta tag,\nHá 50 tags personalizadas criadas em seu Usuario,\n Você pode excluir algumas na opção de editar informações",
                                        31))
                                else:
                                    self.adicionar_tag(tag, atividade, usuario)

                        if opcao3 == '6':
                            novo = input("Novo Conteudo: ")
                            atividade.set_conteudo(novo, usuario)

                    else:
                        print(mudar_cor("Atividade Não Existe", 31))
                else:
                    print(mudar_cor("Esta Disciplina Não Existe", 31))

        elif opcao2 != 'x':
            print(mudar_cor("\nOpção Não Valida", 31))
        return opcao2

