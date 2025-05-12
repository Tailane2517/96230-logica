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

class Endereco:
    logadouro: str
    numero: int
    cidade: str
    estado:str
    def dados_endereco(self):
        print(f"logadouro: {self.logadouro}, numero: {self.numero}, cidade{self.cidade}, estado: {self.estado}")

lista_aluno = []
lista_endereco = []

def dados_aluno(lista_aluno):
    aluno = Aluno(
        nome = input("Digite seu nome: "),
        data_de_nascimento = input("Digite sua data de nascimento: "),
        ra = input("Digite seu RA: "),
        curso = input("Digite o seu curso: "),
        endereco = input("Digite seu endereço: ")
    )
    lista_aluno.append(aluno)

def mostrar_alunos(lista_aluno):
    print("\n Lista de alunos ")
    for aluno in lista_aluno:
        print(f"Nome: {aluno.nome}, data_de_nascimento: {aluno.data_de_nascimento}, ra: {aluno.ra}, curso: {aluno.curso}, endereco: {aluno.endereco} ")

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
    dados_antigos = input("Digite o nome que deseja atualizar: ")
    if dados_antigos in lista_alunos







def dados_endereco(lista_endereco):
    endereco = Endereco(
        logadouro = input("Diigite seu logadouro: "),
        numero = input("Digite seu número: "),
        cidade = input("Digite sua cidade: "),
    )
    lista_endereco.append(endereco)

