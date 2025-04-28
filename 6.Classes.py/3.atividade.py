import os
from dataclasses import dataclass
os.system("cls || clear")

@dataclass
class Pessoa:
    nome: str
    email: str
    telefone: int
    endereco: int

    def exibindo_dados(self): 
        print(f"Nome: {self.nome}, Email: {self.email}, Telefone: {self.telefone}, Endereco: {self.endereco}")




print("Digitando Dados")
nome = input("Digite seu nome:")
email = input("Digite seu email: ")
telefone = input("Digite seu telefone: ")
endereco = input("Digite sua endereco:")

pessoa1 = Pessoa (nome, email, telefone, endereco)
pessoa1.exibindo_dados()


