import os
os.system('clear')

valor_produto = float(input("Digite o valor do produto: "))
forma_de_pagamento = int(input("""
Formas de pagamento                               
1 - Á vista
2 - Á prazo 
                               
Digite a forma de pagamento:"""))     

match forma_de_pagamento:
    case 1:
        print("Á vista desconto = valor_produto * 0.10")
        
    case 2:
        ...
    


