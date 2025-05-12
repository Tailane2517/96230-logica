import os
import time
from dataclasses import dataclass

os.system("cls || clear")

lista_nome = []

@dataclass
class Funcionarios:
    nome: str
    data_de_nascimento: str
    cpf: str
    funcao: str

    def exibir_dados(self):
        print(f"Nome: {self.nome}, data_de_nascimento: {self.data_de_nascimento}, Cpf: {self.cpf}, funcao: {self.funcao}")


lista_funcionarios = []

def verificar_lista_vazia(lista_funcionarios):
    if not lista_funcionarios:
        return True
    return False

def nome_dados(lista_funcionarios):
    funcionario = Funcionarios(
        nome = input("Digite seu nome: "),
    data_de_nascimento = input("Digite sua data de nascimento: "),
    cpf = input("Digite seu CPF: "),
    funcao = input("Digite a sua função: ")
    )
    lista_funcionarios.append(funcionario)
 

def mostrar_dados(lista_funcionarios):
    print("\n - Lista de nomes - ")
    for funcionario in lista_funcionarios:
        print(f"- {funcionario.nome}, {funcionario.data_de_nascimento}, {funcionario.cpf}, {funcionario.funcao}")

def excluir_nome(lista_funcionarios):
    if verificar_lista_vazia(lista_funcionarios):
        print("\nA lista está vazia.")
        return

    mostrar_dados(lista_funcionarios)
    dados_remover = input("Digite o  que deseja remover: ")
    if dados_remover in lista_funcionarios:
        lista_funcionarios.remove(dados_remover)
        print(f"{dados_remover} foi removido com sucesso.")
    else:
        print(f"Os dados {dados_remover} não foram encontrados.")

def atualizar_dados(lista_funcionarios):
    if verificar_lista_vazia(lista_funcionarios):
        print("\nA lista está vazia.")
        return
    
    mostrar_dados(lista_funcionarios)
    dados_antigos = input("Digite o nome que deseja atualizar: ")
    if dados_antigos in lista_funcionarios:
        dados_novos = input(f"Digite o novo nome para {dados_antigos}: ")
        indice = lista_funcionarios.index(dados_antigos)
        lista_funcionarios[indice] = dados_novos
        print(f"{dados_antigos} foi atualizado para {dados_novos}.")
    else:
        print(f"\nO nome {dados_antigos} não foi encontrado.")






while True:
    print("""
    - Gerenciador de nomes -
    1 - Adicionar
    2 - Listar nomes
    3 - Atualizar
    4 - Remover
    5 - Sair
    """)
    opcao = int(input("Digite uma das opções acima: "))

    match opcao:
        case 1:
            nome_dados(lista_funcionarios)
        case 2:
            mostrar_dados(lista_funcionarios)
        case 3:
            atualizar_dados(lista_funcionarios)
        case 4:
            excluir_nome(lista_funcionarios)
        case 5:
            print("\nSaindo do programa.")
            break
        case _:
            print("\nOpção inválida.\nTente novamente.")
    time.sleep(5)
    os.system("cls || clear")