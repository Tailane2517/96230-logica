import os
os.system("clear")

numero_um = float(input("Digite um numero: "))
numero_dois= float(input("Digite um numero: "))

if numero_um < numero_dois:
    menor = numero_um
    maior = numero_dois
else:
    menor = numero_dois
    maior = numero_um

print(f"Menor:  {menor}")
print(f"Maior: {maior}")
