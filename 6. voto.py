import os
os.system('clear')



idade = int(input("Digite a sua idade: "))

def verificar_obrigatoriedade_voto(idade) :
    if 18 <= idade < 65:
        return "Voto obrigatorio"
    elif 16 <= idade < 18 or idade > 65:
        return "Voto opcional"
    else:
        return "Voto obrigatorio"

       
print(f"Idade: {idade} - {verificar_obrigatoriedade_voto(idade)}")