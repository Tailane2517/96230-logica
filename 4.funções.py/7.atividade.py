import os
os.system("csl || clear")



def tabuada(parametro):
    for i in range(1,11):
            print(f"{parametro} x {i} = {numero * i}")
numero = int(input("Digite um número para tabuada: "))

tabuada(numero)