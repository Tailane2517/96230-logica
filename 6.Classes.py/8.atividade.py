import os
from dataclasses import dataclass
os.system("cls || clear")


@dataclass
class Livros:
    nome: str
    autor: str
    categoria: str
    preco: float

    def exibir_dados(self):
        print(f"Nome: {self.nome} \nAutor: {self.autor}\nCategoria: {self.categoria}\nPreço: {self.preco}\n\n")
   
lista_de_livros = []
QUANTIDADE_LIVROS = 3

for i in range(QUANTIDADE_LIVROS):
    livros = Livros(
                nome = input("Digite seu nome: "),
                autor = input("Digite o autor: "),
                categoria = input("Digite a categoria: "),
                preco = float(input("Digite o preço: "))
    )

    lista_de_livros.append(livros)
    print()


nome_arquivo = "catalogo_livros.txt"
with open(nome_arquivo, "a") as catalogo_livros:
    for livros in lista_de_livros:
        catalogo_livros.write(f"Nome: {livros.nome} \nAutor: {livros.autor}\nCategoria: {livros.categoria}\nPreço: {livros.preco}\n\n")
   






for livros in lista_de_livros:
    livros.exibir_dados()