import os
os.system('clear')

sexo = input("Informe o sexo (M para Masculino ou F para Feminino:)")
altura = float(input("Informe a altura em metros: "))

if sexo == "M":
    peso_ideal = (72.7 * altura) - 58
    print(f"\nSeu peso_ideal é: {peso_ideal:} kg")
elif sexo =="F":
    peso_ideal = (62.1 * altura) - 44.7
    print(f"\nSeu peso_ideal é: {peso_ideal:} kg")
else:
    print("\nSexo inválido! Por favor, insira 'M' ou 'F'. ")