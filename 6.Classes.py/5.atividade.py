import os
from dataclasses import dataclass

os.system("cls || clear")

@dataclass
class Endereco:
    logadouro: str
    numero: str
    cidade: str

@dataclass
class Pessoa:
    nome: str
    email: str
    endereco: Endereco #Classe endereço.

    def exibir_dados(self):
        print(f"\tNome: {self.nome} \n"
              f"\tE-mail: {self.email} \n"
              f"\tLogadouro: {self.endereco.logadouro} \n"
              f"\tNúmero: {self.endereco.numero} \n"
              f"\tCidade: {self.endereco.cidade}")

endereco1 = Endereco("Rua A", "33", "Salvador")
pessoa1 = Pessoa("Marta", "marta@gamil.com", endereco1)

pessoa1.exibir_dados()
