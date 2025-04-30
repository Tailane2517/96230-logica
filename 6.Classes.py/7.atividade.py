import os
from dataclasses import dataclass

os.system("csl || clear")

@dataclass
class Pessoa:
    nome: str
    idade: int
    peso : float
    altura: float

    
    def exibir_dados(self):
        print(f"Nome: {self.nome} \nIdade: {self.idade}\nPeso: {self.peso}\nAltura: {self.altura}\n\n")

lista_de_pessoas = []
QUANTIDADE_PESSOAS = 4

for i in range(QUANTIDADE_PESSOAS):
    pessoa = Pessoa(
                nome = input("Digite seu nome: "),
                idade = int(input("Digite sua idade: ")),
                peso = float(input("Digite seu peso: ")),
                altura = float(input("Digite sua altura: "))
            )
    lista_de_pessoas.append(pessoa)

for paciente in lista_de_pessoas:
    pessoa.exibir_dados()