import os
from dataclasses import dataclass
os.system("cls || clear")

@dataclass
class Endereco:
    logadouro: str
    numero: str


@dataclass
class Pessoa:
    #Atributos da classe(variáveis que pertencem a uma classe).
    nome: str
    idade: int
    endereco: Endereco #Classe endereco.

    def exibir_dados(self):
        print(f"Nome:{self.nome},\
              idade:{self.idade},\
              Logadouro:{self.endereco.logadouro},\
              numero:{self.endereco.numero}")
        
endereco1 = Endereco("Rua A", "33")
pessoa1 = Pessoa("Marta", 22, endereco1)

print("Dados da pessoa: ")
pessoa1.exibir_dados()
    