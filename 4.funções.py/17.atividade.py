import os
os.system("cls || clear")

nota = 0

for i in range(1,4):
    nota += float(input("Digite sua nota: "))

def calculando_nota(nota):
    media = nota/3
    return media

media = calculando_nota(nota)

print(f"A sua média é {media}")

if calculando_nota(nota) > 7:
    print(f"A sua média é: {calculando_nota(nota)}")
    print("Aprovado")
else:
    print(f"A média é {calculando_nota(nota)} ")
    print("Reprovado")
