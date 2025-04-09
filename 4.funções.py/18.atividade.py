import os
os.system("cls || clear")

peso = 0
altura = 0

peso = float(input("Digite seu peso: "))
altura = float(input("Digite sua altura: "))

def calculo_do_imc(peso, altura):
    imc = peso / altura ** 2
    return imc

massa = calculo_do_imc(peso, altura)

if massa < 18.5:
        resultado = "Abaixo do peso"
elif massa >= 18.5 and massa <= 24.9:
        resultado = "Peso normal"
elif massa >= 25 and massa <+ 29.9:
        resultado = "Sobrepeso"
elif massa >= 30 and massa <+ 34.9:
        resultado = "Sobrepeso"
elif massa >= 35 and massa <+ 39.9:
        resultado = "Sobrepeso"
elif massa >= :
        resultado = "Sobrepeso"


print(f"O IMC é: {calculo_do_imc(peso, altura):.2f}")