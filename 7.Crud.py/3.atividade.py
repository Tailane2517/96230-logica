import os
from dataclasses import dataclass
os.system("cls || clear")

@dataclass
class Aluno:
    nome: str
    data_de_nascimento: str
    ra: str
    curso: str
    endereco: str
    def dados_aluno(self):
        print(f"Nome: {self.nome}, data_de_nascimento: {self.data_de_nascimento}, ra: {self.ra}, curso: {self.curso}, endereco: {self.endereco} ")
        
@dataclass
class Endereco:
    logadouro: str
    numero: int
    cidade: str
    estado:str
    def dados_endereco(self):
        print(f"logadouro: {self.logadouro}, numero: {self.numero}, cidade{self.cidade}, estado: {self.estado}")

lista_aluno = []


def verificar_lista_vazia(lista_aluno):
    if not lista_aluno:
        return True
    return False


def dados_aluno(lista_aluno):
    aluno = Aluno(
        nome = input("Digite seu nome: "),
        data_de_nascimento = input("Digite sua data de nascimento: "),
        ra = input("Digite seu RA: "),
        curso = input("Digite o seu curso: "),
        endereco = input("Digite seu endereço: ")
    )
    endereco = Endereco(
        logadouro = input("Diigite seu logadouro: "),
        numero = input("Digite seu número: "),
        cidade = input("Digite sua cidade: "),
        estado = input("Digite o seu estado: ")
    )
    lista_aluno.append((aluno,endereco))


def mostrar_alunos(lista_aluno):
    print("\n Lista de alunos ")
    for aluno, endereco in lista_aluno:
        print(f"- Nome: {aluno.nome}, data_de_nascimento: {aluno.data_de_nascimento}, ra: {aluno.ra}, curso: {aluno.curso}, endereco: {aluno.endereco}  logadouro: {endereco.logadouro}, numero: {endereco.numero}, cidade: {endereco.cidade},estado: {endereco.estado} ")

def excluir_aluno(lista_aluno):
    dados_aluno (lista_aluno)
    dados_remover = input("Digite o que deseja remover: ")
    if dados_remover in lista_aluno:
        lista_aluno.remove(dados_remover)
        print(f"{dados_remover} foi removido com sucesso.")
    else:
        print(f"Os dados {dados_remover} não foram encontrados.")

def atualizar_dados(lista_aluno):
    mostrar_alunos(lista_aluno)

    nome_antigo = input("Digite o nome que deseja atualizar: ")
    if nome_antigo in lista_aluno:
        nome = input(f"Digite o novo nome para {nome_antigo}: ")
        data_de_nascimento = input("Digite a nova data de nascimento: ")
        ra = input("Digite o novo RA: ")
        curso = input("Digite o novo curso: ")
        endereco = input("Digite o novo endereço: ")
        logadouro = input("Digite o logadouro atualizado: ")
        numero = input("Digite o novo número: ")
        cidade = ("Digite a cidade atual: ")
        estado = input("Digite o estado atual: ")

        endereco = Endereco(logadouro, numero, cidade, estado)
        lista_aluno[nome_antigo] = Aluno(nome, data_de_nascimento, ra, curso, endereco)
       
        print(f"Dados atualizados com sucesso .")
    else:
        print(f"\nO nome {nome_antigo} não foi encontrado.")


while True:
    print("""
    - Gerenciador de alunos -
    1 - Adicionar alunos
    2 - Listar nomes
    3 - Atualizar
    4 - Remover
    5 - Sair
    """)
    opcao = int(input("Digite uma das opções acima: "))

    match opcao:
        case 1:
            dados_aluno(lista_aluno)
        case 2:
            mostrar_alunos(lista_aluno)
        case 3:
            atualizar_dados(lista_aluno)
        case 4:
            excluir_aluno(lista_aluno)
        case 5:
            print("\nSaindo do programa.")
            break
        case _:
            print("\nOpção inválida.\nTente novamente.")
    
    os.system("cls || clear")










