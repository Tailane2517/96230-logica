import os
os.system("cls || clear")


def inflacao(preco_do_produto):
    if preco_do_produto < 100:
       resultado = preco_do_produto * 1.10
       
    else:
        resultado = preco_do_produto * 1.20
    return resultado    

def descontar(preco_do_produto):
    if preco_do_produto < 100:
        resultado = preco_do_produto * 0.90
    else:
        resultado = preco_do_produto *0.80
    return resultado


preco_do_produto = float(input("Digite um preço: "))
preco_inflacionado = inflacao(preco_do_produto)
preco_do_desconto = descontar(preco_do_produto)

print(f"Preço com aumento: {preco_inflacionado}")
print(f"Valor do desconto: {preco_do_desconto}")