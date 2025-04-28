import os
os.system("cls || clear")

lista_pratos = []
precos_pratos = []

while True:

    opcao = int(input("""
    Código \t Prato \t Valor
    1 \t Picanha \t\t R$ 25,00
    2 \t Lasanha \t\t R$20,00
    3 \t Strogonoff \t\t R$18,00
    4 \t Bife acebolado \t R$15,00
    5 \t Pão com ovo \t\t R$5,00
                    
    Digite a opção desejada:
                    """))
    match opcao:
        case 1:
            prato = "Picanha" 
            preco = 25,00
        case 2 :
            prato = "Lasanha"
            preco = 20,00
        case 3:
            prato = "Strogonoff"
            preco = 18,00
        case 4:
            prato = "Bife Acebolado"
            preco = 15,00
        case 5:
            prato = "Pão com ovo"
            preco = 5,00
        case _:
            prato = "Opção inválida"
            preco = 0


    lista_pratos.append(prato)       
    precos_pratos.append(preco)
        

    continuar = input("Deseja escolher outro prato? \nDigite 'S' ou 'N': ").lower()
    if continuar == "n":
        break




for precos_prato in lista_pratos:
    print(f"Prato: {prato}")

print(f"Total da conta: {sum(precos_pratos):.2f}")