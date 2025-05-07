import os
from dataclasses import dataclass
os.system("cls || clear")

@dataclass
class Funcionario:
    nome: str
    data_de_admissao: str
    matricula: str
    endereco: str

    def exibir_dados(self):
            print(f"Nome: {self.nome}, data_de_emissao: {self.data_de_admissao}, Matricula: {self.matricula}, Endereco: {self.endereco}")


@dataclass
class Cliente:
    nome: str
    data_de_nascimento: str
    endereco: str

    def exibir_dados(self):
        print(f" Nome: {self.nome}, Data_de_nascimento: {self.data_de_nascimento}, Endereco: {self.endereco}")

lista_funcionarios = []
lista_clientes = []
QUANTIDADE_FUNCIONARIOS = 3
QUANTIDADE_CLIENTES = 3

for i in range(QUANTIDADE_FUNCIONARIOS):
    funcionarios = Funcionario(
        nome = input("Digite seu nome: "),
        data_de_admissao = input("Digite a data de admissão: "),
        matricula = input("Digite sua matrícula: "),
        endereco = str(input("Digite seu endereço: "))
    )
    lista_funcionarios.append(funcionarios)
    print()


for i in range(QUANTIDADE_CLIENTES):
    clientes = Cliente(
                nome = input("Digite seu nome: "),
                data_de_nascimento = input("Digite sua data de nascimento: "),
                endereco = input("Digite seu endereço: ")

    )    
    lista_clientes.append(clientes)
    print()


def salvando_arquivo(Cliente):
    nome_arquivo = "Clientes.txt"
    with open(nome_arquivo, "w") as catalogo_clientes:
        for clientes in lista_clientes:
            catalogo_clientes.write(f"Nome: {clientes.nome}, Data_de_nascimento: {clientes.data_de_nascimento}, Endereço: {clientes.endereco}")

arquivo_clienete = salvando_arquivo(Cliente)


def salvando_arquivo(Funcionario):
    nome_arquivo = "Funcionarios2.txt"
    with open(nome_arquivo, "w") as catalogo_dados:
        for funcionarios in lista_funcionarios:
            catalogo_dados.write(f"Nome: {funcionarios.nome}, data_de_admissão: {funcionarios.data_de_admissao}, Matrícula: {funcionarios.matricula}, Endereço: {funcionarios.endereco}")    

arquivo = salvando_arquivo(Funcionario)

