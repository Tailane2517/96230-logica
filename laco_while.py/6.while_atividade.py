import os
os.system("cls || clear")

login = 0
senha = 0

login_cadrastrado = "tailane"
senha_cadastrada = "1234"

for i in range(3):
        login = input("Digite o login: ")
        senha = input("Digite a senha: ")

        if  login_cadrastrado == login and  senha_cadastrada == senha:
             print("Bem-Vindo!")
             break
        else:
         print("Senha ou login incorreto. \n") 
        if i == 2:
           print("Número de tentativas acima do permitido.")  
             

          




