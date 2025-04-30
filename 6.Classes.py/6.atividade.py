import os
from dataclasses import dataclass

os.system("csl || clear")

@dataclass
class Paciente:
    #Atributos: são variáveis que pertencem a classe.
    nome: str
    idade: int

    #Método: é uma função que pertence a classe.
    #Este método para exibir dados do paciente.
    def exibir_dados(self):
        print(f"Nome: {self.nome} \nIdade: {self.idade}\n\n")

lista_de_pacientes = []
QUANTIDADE_PACIENTES = 2
#Atribuindo dados ao paciente1.
for i in range(QUANTIDADE_PACIENTES):
    paciente = Paciente(
                    nome = input("Digite seu nome: "),
                    idade = int(input("Digite sua idade: "))
                )
    lista_de_pacientes.append(paciente)
    print()


#Salvando em um arquivo com .txt
nome_arquivo = "Dados_paciente.txt"
with open(nome_arquivo, "a") as arquivo_pacientes:
    for paciente in lista_de_pacientes:
        arquivo_pacientes.write(f"{paciente.nome}, {paciente.idade}\n")

print("Dados salvos com sucesso.")


for paciente in lista_de_pacientes:
    paciente.exibir_dados()