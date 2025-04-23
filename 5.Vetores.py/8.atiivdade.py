import os
os.system("cls || clear")

QUANTIDADE_NUMEROS = 5
lista_numeros =[]


def solicitar_numeros():
    for i in range(QUANTIDADE_NUMEROS):
        numero = int(input("Digite o primeiro numero: "))
        lista_numeros.append(numero)
    return lista_numeros


def negativo_positivo(lista_numeros):
    negativo = 0
    positivo = 0
    for numero in lista_numeros:
        if numero <0:
            negativo += 1
        else :
            positivo += numero
    return negativo, positivo



for numero in lista_numeros:
    print(numero)



lista_numeros = solicitar_numeros()
negativo, positivo = negativo_positivo(lista_numeros)



print(f"Soma dos números positivos: {positivo}")
print(f"Quantidade de números negativos: {negativo}")