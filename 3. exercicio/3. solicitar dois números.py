import os
os.system("clear")

primeiro_numero = float(input("Digite sua primeira nota: "))
segundo_numero = float(input("Digite a segunda nota: "))

soma = primeiro_numero + segundo_numero 
media = soma / 2
produto = primeiro_numero * segundo_numero


if primeiro_numero < segundo_numero:
    menor = primeiro_numero
    maior = segundo_numero
else: 
    menor = primeiro_numero
    maior = segundo_numero

print("\nExibindo resultados: ")
print(f"Média: {media}")
print(f"Produto: {produto}")
print(f"Menor: {menor}")
print(f"Maior: {maior}")

 