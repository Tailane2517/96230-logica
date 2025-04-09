import os
os.system("cls || clear")

def calcular(n1,n2):
    somar = n1 + n2
    subtrair = n1 - n2
    return somar, subtrair

n1 = int(input("Digite o primeiro número: "))
n2 = int(input("Digite o segundo número: "))

soma , subtracao = calcular(n1, n2)

print(f"Soma: {soma}")
print(f"Subtração: {subtracao}")
