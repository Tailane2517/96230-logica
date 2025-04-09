import os
os.system("cls || clear")

nota = 0
for i in range(1,4):
    nota += float(input("Digite a nota: "))

def calculo(nota):
    media = nota/3
    return media

calculando =calculo(nota)

print(f"A sua média é: {calculando}")


