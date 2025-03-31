import os
import time

os.system("cls || clear")


contador = 0
soma_salario = 0
maior_idade = 0
menor_idade = 0
mulheres5k= 0

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
            nome = input("Digite o nome: ")
            idade = int(input("Digite sua idade:"))
            sexo = input("""Digite seu sexo - Use 'M' ou 'F': """).upper()
            salario = float(input("Digite seu salário: "))
            contador += 1
            soma_salario += salario
            maior_idade = max(maior_idade, idade)
            menor_idade = min(menor_idade, idade)
            if sexo == "F" and salario >= 5000:
                mulheres5k += 1
        case 2:
            if contador > 0:
                media_salarial = soma_salario / contador
                print("\n= Exibindo resultados =")
                print(f"Média salarial grupo: {media_salarial}")
                print(f"Maior idade do grupo: {maior_idade}")
                print(f"Menor idade do grupo: {menor_idade}")
                print(f"Quantidade de mulheres com salario a partir de 5k: {mulheres5k}")
            else: 
                print("\nNão foram informados os dados necessários.")
            time.sleep(3)
            os.system("cls || clear")
        case 3:
            print("\n= FIM =")
            break
        case _:
            print("\nOpção inválida.")
            time.sleep(3)
            os.system("cls || clear")

            

             

        
                                              
            

                
               
                
                
            
            

