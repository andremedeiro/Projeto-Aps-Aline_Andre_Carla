from atividade import Atividade
from usuario import Usuario
from disciplina import Disciplina

adm = Usuario("admin","123","André")
disciplina = Disciplina("portugues", "Tássia Regis")
adm.adicionar_disciplina(disciplina)

class Sistema:
    def __init__(self):
        self.usuarios = [adm]
#______________________________________________________________________
#  METODOS SOBRE USUARIO
    def cadastrar_usuario(self, email, senha, nome):
        usuario = Usuario(email, senha, nome)
        self.usuarios.append(usuario)

    def remover_usuario(self, nome_usuario):
        usuario = self.buscar_usuario(nome_usuario)
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
                return (email)

    def logar(self, email, senha):
        if len(self.usuarios) == 0:
            print("Nenhum Usuario Cadastrado")
        else:
            for usuario in self.usuarios:
                if email == usuario.get_email():
                    if senha == usuario.get_senha():
                        print("\nLogado com Sucesso")
                        opcao2 = ''
                        while opcao2 != 'x':
                            opcao2 = self.menu_logado(usuario)
                    else:
                        print("Senha Incorreta")
                else:
                    print("\nEmail e/ou Senha incorreta")
#_________________________________________________________________________
#     METODOS SOBRE ATIVIDADE

    def criar_atividade(self, nome, data_final, disciplina, tags, usuario):
        disciplina.adicionar_atividade(Atividade(nome, data_final, disciplina, tags))

    def listar_atividades(self, usuario):
        for disciplina in usuario.disciplinas:
            disciplina.listar_atividades()

    def mudar_cor(self, texto, cor):
        return str('\033[' + str(cor) + 'm' + str(texto) + '\033[0;0m')

#__________________________________________________________________________________
#      METODOS SOBRE DISCIPLINA

    def buscar_disciplina(self, nome, usuario):
        for disciplina in usuario.disciplinas:
            if disciplina.get_nome() == nome:
                return disciplina

    def criar_disciplina(self,nome,professor, usuario):
        disciplina = Disciplina(nome, professor)
        usuario.adicionar_disciplina(disciplina)


#___________________________________________________________________________________
#                        MENUS
    def menu(self):
        print("\n1 - Cadastrar Usuario")
        print("2 - Listar Usuarios")
        print("3 - Logar")
        print('x - Sair')
        opcao = input("Digite a opção desejada: ")

        if opcao == '1':
            email = str(input("\nEmail: "))
            senha = str(input("Senha: "))
            nome = str(input("Nome: "))
            self.cadastrar_usuario(email, senha, nome)

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
        print("1 - Remover Conta")
        print("2 - Criar Disciplina")
        print("3 - Listar Disciplinas")
        print("4 - Criar Atividade")
        print("5 - Listar Atividades")
        print('x - Sair')
        opcao2 = input("Digite a opção desejada: ")

        if opcao2 == '1':
            self.remover_usuario(usuario.get_nome())
            opcao2 = 'x'

        elif opcao2 == '2':
            nome=input("Nome da Disciplina: ")
            if self.buscar_disciplina(nome, usuario) == None:
                professor=input("Professor da Disciplina: ")
                self.criar_disciplina(nome, professor, usuario)
            else:
                print("Disciplina já existente")

        elif opcao2 == '3':
            usuario.listar_disciplinas()

        elif opcao2 == '4':
            disciplina = input("De qual Disciplina é esta Atividade? ")
            disciplina = self.buscar_disciplina(disciplina, usuario)
            if disciplina != None:
                nome=input("Nome da Atividade: ")
                data_final=input("Prazo da atividade(DD/MM/AAAA): ")
                tags=input("Tags da atividade(separadas por espaço): ").split(' ')
                self.criar_atividade(nome, data_final, disciplina, tags, usuario)

            else:
                print("Disciplina não existente")

        elif opcao2 == '5':
            usuario.listar_atividades()

        return opcao2
