import os
from dataclasses import dataclass
os.system("cls || clear")


@dataclass
class Dados:
    nome: str
    data_de_nascimento: int
    rg: int
    cpf: int

    def exibir_dados(self):
        print(f"Nome: {self.nome} \nData_de_nascimento: {self.data_de_nascimento}\nRG: {self.rg}\nCPF: {self.cpf}\n\n")
   
lista_de_dados = []
QUANTIDADE_DADOS = 5

for i in range(QUANTIDADE_DADOS):
    dados = Dados(
                nome = input("Digite seu nome: "),
                data_de_nascimento = int(input("Digite sua data de nascimento: ")),
                rg = input("Digite o seu RG: "),
                cpf = int(input("Digite o seu CPF: "))
    )

    lista_de_dados.append(dados)
    print()


nome_arquivo = "Funcionarios.txt"
with open(nome_arquivo, "a") as catalogo_dados:
    for dados in lista_de_dados:
        catalogo_dados.write(f"Nome: {dados.nome} \nData_de_nascimento: {dados.data_de_nascimento}\nRG: {dados.rg}\nCPF: {dados.cpf}\n\n")
   






for dados in lista_de_dados:
    dados.exibir_dados()