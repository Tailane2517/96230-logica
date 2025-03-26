import os
os.system("cls || clear")

soma = 0
contador = 0

while True:
    numero_inteiro = int(input("Digite um numero: "))
    
    if numero_inteiro <0:
        break
    else:
        contador += 1
        soma += numero_inteiro
        media = numero_inteiro/soma

if contador == 0:
    soma = numero_inteiro
    contador =1


print(f"Media: {media}")