import os
os.system("cls || clear")

soma = 0

for i in range(3):
    nota = float(input("Digite sua nota: "))
    soma += nota

    media = soma/3
    
if media >= 7:
    print("Você está aprovado!")
elif  media < 7 and media >=4:
    print("Você foi reprovado!")
else: 
    print("Você está de recuperação")



