import os
os.system("cls || clear")

QUANTIDADE_NÚMEROS = 6
lista_numeros = []

def pares_e_impares(lista_numeros):
    pares = 0
    impares = 0
    for numero in lista_numeros:
        if numero % 2 == 0:
            pares += 1
        else:
            impares += 1
    return pares, impares

for i in range(QUANTIDADE_NÚMEROS):
    numero = int(input("Digite um número: "))
    lista_numeros.append(numero)
        
for numero in lista_numeros:
    print(numero)

pares, impares = pares_e_impares(lista_numeros)


print(f"Pares: {pares}")
print(f"Impares: {impares}")

    