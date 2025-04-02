import os
os.system("cls || clear")



def logo_senai():
    os.system("cls || clear ")
    print("== SENAI DENDEZEIROS ==")

def somar(primeiro_numero, segundo_numero):
    return primeiro_numero + segundo_numero

def subtrair(primeiro_numero, segundo_numero):
    return primeiro_numero - segundo_numero

def multiplicar(primeiro_numero, segundo_numero):
    return primeiro_numero * segundo_numero

def dividir(primeiro_numero, segundo_numero):
    return primeiro_numero / segundo_numero

logo_senai()
primeiro_numero = int(input("Digite o primeiro número: "))

logo_senai()
segundo_numero = int(input("Digite o segundo número: "))

soma = somar(primeiro_numero, segundo_numero)
subtracao = subtrair(primeiro_numero, segundo_numero)
multiplicacao = multiplicar(primeiro_numero, segundo_numero)
divisao = dividir(primeiro_numero, segundo_numero)


logo_senai()
print(f"Soma: {soma}")
print(f"Subtração: {subtracao}")
print(f"Multiplicação: {multiplicacao}")
print(f"Divisão: {divisao}")
