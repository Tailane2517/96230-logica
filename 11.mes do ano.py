import os
os.system('clear')

mes_do_ano = int(input(""" 
Mês 
1 \t Janeiro
2 \t Fevereiro
3 \t Março
4 \t Abril
5 \t Maio
6 \t Junho
7 \t Julho
8 \t Agosto
9 \t Setembro
10 \t Outubro
11 \t Novembro
12 \t Dezembro

Digite o mês do ano: 
"""))

match mes_do_ano:
    case 1:
        print("Janeiro")
    case 2:
        print("Fevereiro")
    case 3:
        print("Março")
    case 4:
        print("Abril")
    case 5:
        print("Maio")
    case 6:
        print("Junho") 
    case 7:
        print("Julho")
    case 8:
        print("Agosto")
    case 9:
        print("Setembro")
    case 10:
        print("Outubro")
    case 11:
        print("Novembro")
    case 12:
        print("Dezembro")   