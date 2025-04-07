import os
os.system("cls || clear")

def posistivo_negativo(numero):
    if numero < 0:
        print("Número negativo.")
    elif numero == 0:
        print("Número neutro.")
    else:
        print("Número positivo.")

numero = int(input("Digite um número:"))
posistivo_negativo(numero)