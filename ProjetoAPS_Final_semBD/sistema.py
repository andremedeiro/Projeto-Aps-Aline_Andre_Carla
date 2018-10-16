from atividade import Atividade
from usuario import Usuario
from disciplina import Disciplina
'''
Sempre que não existir ou ja exisitr uma disciplina, atividade, ou usuario com o nome informado, pergute se deseja fazer outro

Falta ordenar a listagem de de atividades por data


'''
class Sistema:
    def __init__(self):
        self.usuarios = [adm]
        self.tags_programadas = ["Projeto","Prova", "Mini-teste", "Monitoria", "Seminário"]


    # ______________________________________________________________________
    #  METODOS SOBRE USUARIO
    def cadastrar_usuario(self, email, senha, nome):
        usuario = Usuario(email, senha, nome)
        self.usuarios.append(usuario)

    def remover_usuario(self, usuario):
        self.usuarios.remove(usuario)

    def listar_usuarios(self):
        if len(self.usuarios) == 0:
            print("Nenhum Usuario Cadastrado")
        else:
            for usuario in self.usuarios:
                print(" ")
                print(usuario)

    def buscar_usuario(self, email):
        for usuario in self.usuarios:
            if usuario.get_email() == email:
                return (usuario)

    def logar(self, email, senha):
        if len(self.usuarios) == 0:
            print("Nenhum Usuario Cadastrado")
        else:
            usuario = self.buscar_usuario(email)
            if usuario != None:
                if senha == usuario.get_senha():
                    print(self.mudar_cor("Logado Com Sucesso", 32))
                    opcao2 = ''
                    while opcao2 != 'x':
                            opcao2 = self.menu_logado(usuario)
                else:
                    print(self.mudar_cor("Senha Incorreta", 31))
            else:
                print(self.mudar_cor("Não foi encontrado nenhum usuario com este email", 31))

    # _________________________________________________________________________
    #     METODOS SOBRE ATIVIDADE

    def adicionar_tag(self, tag, atividade, usuario):
        if tag in self.tags_programadas:
            atividade.adicionar_tag(tag)

        elif tag not in usuario.tags_personalizadas:
            usuario.adicionar_tag(tag)
            atividade.adicionar_tag(tag)

    def criar_atividade(self, nome, data_final, conteudo, disciplina, id, usuario):
        disciplina.adicionar_atividade(Atividade(nome, data_final, conteudo, disciplina, id))

    def listar_atividades(self, usuario):
        for disciplina in usuario.disciplinas:
            disciplina.listar_atividades()

    def buscar_atividade(self, id, usuario):
        for disciplina in usuario.disciplinas:
            for atividade in disciplina.atividades:
                if atividade.get_id() == id:
                    return (atividade)

    def remover_atividade(self, atividade_excluir, usuario):
        for disciplina in usuario.disciplinas:
            for atividade in disciplina.atividades:
                if atividade == atividade_excluir:
                    disciplina.atividades.remove(atividade_excluir)
                else:
                    print(self.mudar_cor("Atividade Não Existe", 31))

    def concluir_atividade(self, atividade, usuario):
        atividade.set_situacao("Atividade Concluida")

    def arquivar_atividade(self, atividade_excluir, usuario):
        for disciplina in usuario.disciplinas:
            for atividade in disciplina.atividades:
                if atividade == atividade_excluir:
                    disciplina.atividades.remove(atividade_excluir)
                    disciplina.adicionar_atividade_arquivada(atividade_excluir)
                else:
                    print(self.mudar_cor("Atividade Não Existe", 31))

    def mudar_cor(self, texto, cor):
        return str('\033[' + str(cor) + 'm' + str(texto) + '\033[0;0m')

    # __________________________________________________________________________________
    #      METODOS SOBRE DISCIPLINA

    def buscar_disciplina(self, nome, usuario):
        for disciplina in usuario.disciplinas:
            if disciplina.get_nome() == nome:
                return disciplina

    def criar_disciplina(self, nome, professor, usuario):
        disciplina = Disciplina(nome, professor)
        usuario.adicionar_disciplina(disciplina)

    # ___________________________________________________________________________________
    #                        MENUS
    def menu(self):
        print("1 - Cadastrar Usuario")
        print("2 - Listar Usuarios")
        print("3 - Logar")
        print('x - Sair')
        opcao = input("Digite a opção desejada: ")

        if opcao == '1':
            email = str(input("\nEmail: "))
            if self.buscar_usuario(email) == None:
                senha = str(input("Senha: "))
                nome = str(input("Nome: "))
                self.cadastrar_usuario(email, senha, nome)
            else:
                print(self.mudar_cor("Úsuario Já Existe", 31))

        elif opcao == '2':
            print("\nUsuarios: ")
            self.listar_usuarios()

        elif opcao == '3':
            print("\nLogar")
            email = str(input("Email: "))
            senha = str(input("Senha: "))
            self.logar(email, senha)
        return opcao

    def menu_logado(self, usuario):
        print("")
        print("--------------------HOME--------------------")
        usuario.listar_atividades()
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
            if self.buscar_disciplina(nome, usuario) == None:
                professor = input("Professor da Disciplina: ")
                self.criar_disciplina(nome, professor, usuario)
            else:
                print(self.mudar_cor("Disciplina Já Existe", 31))

        elif opcao2 == '3':
                usuario.listar_disciplinas()

        elif opcao2 == '4':
            disciplina = input("De qual Disciplina é esta Atividade? ")
            disciplina = self.buscar_disciplina(disciplina, usuario)
            if disciplina != None:
                nome = input("Nome da Atividade: ")
                id = input("Informe um número para identifica-la: ")
                if self.buscar_atividade(id, usuario) == None:
                    data_final = input("Prazo da atividade(DD/MM/AAAA): ")
                    conteudo = input('Conteudo: ')
                    self.criar_atividade(nome, data_final, conteudo, disciplina, id, usuario)
                    atividade = self.buscar_atividade(id, usuario)
                    adicionar = input("Deseja adicionar alguma Tag? ")
                    while adicionar != 'nao':
                        if len(usuario.get_tags_personalizdas()) < 50:
                            tag = input("Tag: ")
                            self.adicionar_tag(tag, atividade, usuario)
                            adicionar = input("Adicionar mais uma? ")
                        else:
                            print(self.mudar_cor("Não foi possivel adicionar mais tags,\nHá 50 tags personalizadas criadas em seu Usuario", 31))
                            break
                else:
                    print(self.mudar_cor("ID já Existe", 31))

            else:
                print(self.mudar_cor("Disciplina Não Existe", 31))

        elif opcao2 == '5':
            usuario.listar_atividades_arquivadas()

        elif opcao2 == '6':
            id = input("Informe o ID da Atividade: ")
            atividade = self.buscar_atividade(id, usuario)
            if atividade != None:
                atitude = input(
                    "Deseja excluir a atividade " + atividade.get_nome() + "? (Digite " + "sim" + " para exluir) ")

                if atitude == "sim":
                    print(self.mudar_cor("A Atividade " + str(atividade.get_nome()) + " Foi Excluida com Sucesso", 32))
                    self.remover_atividade(atividade, usuario)

                else:
                    print(self.mudar_cor(
                        "A Atividade " + str(atividade.get_nome()) + " Foi Arquivada e Concluida com Sucesso", 32))
                    self.concluir_atividade(atividade, usuario)
                    self.arquivar_atividade(atividade, usuario)


            else:
                print(self.mudar_cor("Atividade Não Existe", 31))

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
                        usuario.set_email(novo)

                    else:
                        print(self.mudar_cor("Email em Uso", 31))

                elif opcao3 == '3':
                    novo = input("Digite a nova Senha: ")
                    confirmar = input("Confirme a Senha Digitada: ")
                    if novo == confirmar:
                        usuario.set_senha(novo)
                    else:
                        print(self.mudar_cor("Senhas Não Coincidem", 31))

                elif opcao3 == '4':
                    if len(usuario.get_tags_personalizdas()) != 0:
                        print(usuario.get_tags_personalizdas())
                        excluir=input("Essas são as tags Criadas por você, informe as tags que deseja excluir separando-as por virgula: ").split(",")
                        for tag in excluir:
                            usuario.remover_tag(tag)
                    else:
                        print(self.mudar_cor("Não Existem Tags Personalizadas", 31))



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
                        disciplina.set_nome(novo)

                    elif opcao3 == '2':
                        novo = input("Digite o novo Professor: ")
                        disciplina.set_professor(novo)
                else:
                    print(self.mudar_cor("Disciplina Não Existe", 31))

            elif opcao4 == '3':
                ID = input("ID da Atividade que Deseja Editar: ")
                atividade = self.buscar_atividade(ID, usuario)
                if atividade != None:
                    print("1 - Alterar Nome")
                    print("2 - Alterar ID")
                    print("3 - Alterar Disciplina")
                    print("4 - Alterar Data Final")
                    print("5 - Alterar Tags")
                    print("6 - Alterar Conteudo")

                    opcao3 = input("Digite o número para qual atributo deseja alterar: ")
                    print("  ")

                    if opcao3 == '1':
                        novo = input("Digite o novo nome: ")
                        atividade.set_nome(novo)

                    if opcao3 == '2':
                        novo = input("Novo ID: ")
                        teste = self.buscar_atividade(novo, usuario)
                        if teste == None:
                            atividade.set_ID(novo)
                        else:
                            print(self.mudar_cor("ID em Uso", 31))

                    if opcao3 == '3':
                        novo = input("Nova Disciplina: ")
                        disciplina_destino = self.buscar_disciplina(novo, usuario)
                        if disciplina_destino != None:
                            disciplina_destino.adicionar_atividade(atividade)
                            atividade.disciplina.remover_atividade(atividade)
                            atividade.set_disciplina(disciplina_destino)
                        else:
                            print(self.mudar_cor("Disciplina Não Existe", 31))

                    if opcao3 == '4':
                        novo = input("Novo Prazo (DD/MM/AAAA): ")
                        atividade.set_datafinal(novo)
                        atividade.situacao = atividade.analisa_situacao()

                    if opcao3 == '5':
                        adicionar = ''
                        while adicionar != 'nao':
                            if len(usuario.tags_personalizadas) < 50:
                                tag = input("Tag: ")
                                self.adicionar_tag(tag, atividade, usuario)
                                adicionar = input("Mais Alguma? ")
                            else:
                                print(self.mudar_cor(
                                    "Não foi possivel adicionar mais tags,\nHá 50 tags personalizadas criadas em seu Usuario",
                                    31))
                                break

                    if opcao3 == '6':
                        novo = input("Novo Conteudo: ")
                        self.situacao = atividade.set_conteudo(novo)

                else:
                    print(self.mudar_cor("Atividade Não Existe", 31))
        return opcao2

adm = Usuario("andre", "123", "André")
disciplina = Disciplina("portugues", "Tássia Regis")
adm.adicionar_disciplina(disciplina)
atividade = Atividade("Redação", "04/10/2018", "Fazer um Redação do ENEM", disciplina, "15")
disciplina.adicionar_atividade(atividade)
