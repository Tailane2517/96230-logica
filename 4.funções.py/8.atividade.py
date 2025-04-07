import os
os.system("csl || clear")


def numeracao(parametro):
        if numero % 2 == 0:
          print(f"O numero{parametro} é par")
        else:
         print(f"O numero {parametro} é impar")
numero = int(input("Digite um número: "))
numeracao(numero)

