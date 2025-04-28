import os
from dataclasses import dataclass
os.system("cls || clear")

@dataclass
class Pessoa:
    nome: str
    idade: int
    peso: float
    altura: float

#pessoa1 = Pessoa ("Tailane", 18, 61.0, 1.63 )

print("Digitando Dados: ")
nome = input("Digite seu nome:")
idade = int(input("Digite sua idade: "))
peso = float(input("Digite seu peso: "))
altura = float(input("Digite sua altura:"))

#pessoa1 = Pessoa(nome=nome, idade=idade, peso=peso, altura=altura)
pessoa1 = Pessoa (nome, idade, peso, altura)


print(f"Nome: {pessoa1.nome}, idade: {pessoa1.idade}, peso: {pessoa1.peso}, altura: {pessoa1.altura}")