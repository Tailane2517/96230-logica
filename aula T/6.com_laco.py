import os 
import time
os.system("cls || clear")

numero = int(input("Digite um numero: "))
print("CONTAGEM REGRESSIVA")
for i in range(numero, 0,-1):
    print(f"{i}")
    time.sleep(1)