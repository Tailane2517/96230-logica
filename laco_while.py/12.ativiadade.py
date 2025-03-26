import os
os.system("cls || clear")

while True:
    menu = int(input("""
    Código \t Descrição
    1 \t \t Adicionar pessoa"
    2 \t \t Exibir resultados"
    3 \t \t Sair
    Digite uma opção                
    """))

    match menu:
        case 1:
            idade = input("Digite sua idade:")
            sexo = input("Digite seu sexo (F) e (M): ")
            salário = int(input("Digite seu salário: "))
        case 2:
            print("Idade: {idade}")
            print("Sexo: {sexo}")
            print("Salário: {salário}")
        case 3:
            print("FIM")
            break
        case 4:
            print("Opção inválida")

            
            

