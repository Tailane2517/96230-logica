import os
from dataclasses import dataclass

os.system("cls || clear")

@dataclass
class Autor:
    nome : str
    biografia : str

@dataclass
class Livro:
    titulo: str
    ano: int
    autor : Autor
    
    
    def exibir_dados(self):
        print(f"Nome: {self.autor.nome}, Biografia: {self.autor.biografia}, Titulo: {self.titulo}, Ano: {self.ano}, Autor: {self.autor}")


lista_livros = []
QUANTIDADE_LIVROS = 1

print("DADOS")

for i in range(QUANTIDADE_LIVROS):
    livro = Livro(
        titulo =input("Digite o titulo do livro:"),
        ano = int(input("Digite ano de publicação: ")),
        autor = Autor(
            nome =input("Digite o nome do autor: "),
            biografia = input("Digite a biografia:")
        )
    )
    lista_livros.append(livro)

print("\n= Salvando = ")
nome_arquivo = "Autor_Livro.txt"
with open(nome_arquivo, "a") as autor_livros:
    for dados in lista_livros:
        autor_livros.write (f"Nome: {dados.autor.nome}\n Biografia: {dados.autor.biografia}\nTitulo: {dados.titulo}\n Ano: {dados.ano}\n Autor: {dados.autor}")

print("\n= Dados salvos = ")


print("\n= Lendo dados do arquivo =")

try:
    with open(nome_arquivo, "r", encoding="utf-8") as arquivo:
        linhas = arquivo.readlines()
        for linha in linhas:
            print(f"{linha.strip()}")
except FileNotFoundError:
    print("Arquivo não encontrado.")