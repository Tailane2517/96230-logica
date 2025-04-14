import os
os.system("cls || clear")

QUANTIDADE_NUMEROS = 5

lista_numeros = []
for i in range(QUANTIDADE_NUMEROS):
    numero = int(input("Digite um número: "))
    lista_numeros.append(numero)

for numero in lista_numeros:
    print(numero)

maior = max(lista_numeros)
menor = min(lista_numeros)

print(f"Maior: {maior}")
print(f"Menor: {menor}")

