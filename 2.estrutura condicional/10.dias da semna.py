import os
os.system("clear")

dia_da_semana = float(input("Digite o dia da semana: "))

match dia_da_semana:
    case 1:
        print("Hoje é fim de semana")
    case 2:
        print("Hoje é segunda-feira.")
    case 3:
        print("Hoje é terça-feira.")
    case 4:
        print("Hoje é quarta-feira.")
    case 5:
        print("Hoje é quinta-feira.")
    case 6:
        print("Hoje é sexta-feira")
    case 7:
        print("Hoje é fim de semana!")
    case _:
       print("Dia inválido")
       
