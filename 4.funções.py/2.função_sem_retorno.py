import os


# Função sem retorno
def logo_senai():
    os.system("cls || clear ")
    print("== SENAI ==")

logo_senai() # Chamando a função
nome = input("Digite seu nome: ")

logo_senai() # Chamando a função
idade = int(input("Digite sua idade: "))

logo_senai() # Chamando a função
print(f"Nome: {nome}")
print(f"Idade: {idade}")
    