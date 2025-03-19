import os
os.system("cls || clear")

while True:
    nota = float(input("Digite sua nota: "))

    if nota < 10 > 0:
        print("A nota deve ser entre 0 e 10\n")
    else:
        break
print(f"Nota: {nota}")


