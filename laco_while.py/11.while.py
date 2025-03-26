import os
os.system("cls || clear")

soma_pares = 0
soma_impares = 0
pares = 0
impares = 0
contador = 0
soma_geral = 0

while True:
        numero = int(input(f"Digite o {contador + 1}º: "))
        
        if numero == 0:
            break

        if numero % 2 == 0:
            pares += 1
            soma_pares += numero
        else:
            impares += 1
            
        
        contador += 1
        soma_geral += numero

        

media_pares = soma_pares/pares
media_geral = soma_geral/contador

print(f"\nQuantidade de pares: {pares}")
print(f"Quantidade de ímpares: {impares}")
print(f"\nMédia pares: {media_pares}")
print(f"Média geral: {media_geral}")


    