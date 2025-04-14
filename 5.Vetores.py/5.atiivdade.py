import os
os.system("cls || clear")

pares = 0
impares = 0

QUANTIDADE_NUMEROS = 6
lista_numeros = []

for i in range(QUANTIDADE_NUMEROS):
    numero = int(input("Digite o número: "))
    lista_numeros.append(numero)
    if numero % 2 == 0:
        pares += 1
    else:
        impares += 1

for numero in lista_numeros:
    print(numero)

print(f"Pares: {pares}")
print(f"Impares: {impares}")
