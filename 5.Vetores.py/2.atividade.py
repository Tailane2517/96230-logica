import os
os.system("cls || clear")

lista_notas = []
QUANTIDADE_NOTAS = 3

for i in range(QUANTIDADE_NOTAS):
    nota = float(input("Digite uma nota: "))
    lista_notas.append(nota)


media = sum(lista_notas) / QUANTIDADE_NOTAS


print()
for nota in lista_notas:
    print(nota)

print(f"Média: {media}")
