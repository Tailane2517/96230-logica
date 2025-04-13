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

def classificar_imc(massa):     
        if massa < 18.5:
                return  "Abaixo do peso - Consulte um nutricionista para orientação"
        elif massa >= 18.5 and massa <= 24.9:
                 return "Peso normal - Mantenha hábitos saúdaveis!"
        elif massa >= 25 and massa <+ 29.9:
                return  "Sobrepeso - Considere uma dieta balanceada e atividade física."
        elif massa >= 30 and massa <+ 34.9:
                return  "Obesidade grau 1 - Procure orientação de um profissional de saúde"
        elif massa >= 35 and massa <+ 39.9:
                return  "Obesidade grau 2 - Consulte um médico para avaliação e orientação"
        else:
                 return  "Obesidade grau 3 - Busque assistência médica imediatamente"

classificacao = classificar_imc(massa)

print(f"Seu IMC é: {massa:.2f}")
print(classificacao)