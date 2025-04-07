import os
os.system("cls || clear")



def transformando_em_centimetros(metros):
    return metros * 100;

print("= Converter metros para centimetros =")
metros= float(input("Digite um valor: "))


centimetros = transformando_em_centimetros(metros)

print(f"{metros} metros é igual a {centimetros} centimetros.")
