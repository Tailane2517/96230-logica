import os
os.system("cls || clear")

data_de_nascimento = int(input("Digite sua data de nascimento: "))

def ano_de_nascimento(data_de_nascimento):
    os.system("cls || clear")
    resultado = 2025 - data_de_nascimento
    return resultado
    

idade = ano_de_nascimento(data_de_nascimento)



print(f"Data de nascimento: {idade}")
