import os
os.system("cls || clear")



def calculo_media(nota1, nota2):
    soma = nota1 + nota2
    resultado = soma /2
    return resultado

def resultado(media):
    if media >= 7:
        print("Aprovado!")
    else :
        print("Reprovado!")

nota_um = float(input("Digite a nota: "))
nota_dois = float(input("Digite a nota: "))

media = calculo_media(nota_um, nota_dois)
resultado(media)




