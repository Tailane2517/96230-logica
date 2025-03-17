import os
os.system('clear')

valor_produto = float(input("Digite o valor do produto: "))
forma_de_pagamento = int(input("""
Código \t Formas de pagamento:                              
1 - Á vista
2 - Á prazo 
                               
Digite a forma de pagamento:"""))     

match forma_de_pagamento:
    case 1:
       desconto = valor_produto * 0.10
       valor_final = valor_produto - desconto
       print("\nForma de pagamento: À vista")
       print(f"Valor do produto: R$ {valor_produto:.2f}")
       print(f"Valor do desconto: R$ {desconto:.2f}")
       print(f"Total a pagar: R$ {valor_final:.2f}")

        
    case 2:
      print("\Você escolheu pagamento à prazo. ")
      quantidade_parcelas = int(input("Digite a quantidade de parcelas(ate 6): "))
  
      valor_parcela = valor_produto / quantidade_parcelas
      print("\nForma de pagamento: À prazo")
      print(f"Valor do produto: R$ {valor_produto:.2f}")
      print(f"Quantidade de parcelas: {quantidade_parcelas}")
      print(f"Valor por parcela: R$ {valor_parcela:.2f}")
      print(f"Total à prazo: R$ {valor_produto:.2f}")

    case 3:
      print("Quantidade de parcelas inválida. O máximo permitido é 6.")

    case 4:
      print("Opção de pagamento invalido Por favor, tente novamente.")



    


