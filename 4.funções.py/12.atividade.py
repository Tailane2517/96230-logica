import os
os.system("cls || clear")

def logo_senai():
    os.system("cls || clear")

def somar(primeiro_numero, segundo_numero):
    return primeiro_numero + segundo_numero

def multiplicar(primeiro_numero, segundo_numero):
    return primeiro_numero * segundo_numero

def dividir( primeiro_numero, segundo_numero):
    return primeiro_numero / segundo_numero

def subtrair(primeiro_numero, segundo_numero):
    return primeiro_numero - segundo_numero

logo_senai()
primeiro_numero = int(input("Digite o primeiro número: "))

logo_senai()
segundo_numero = int(input("Digite o segundo numero: "))

soma = somar(primeiro_numero, segundo_numero)
subtração = subtrair( primeiro_numero, segundo_numero)
multiplicação = multiplicar(primeiro_numero, segundo_numero)
divisão = dividir(primeiro_numero, segundo_numero)

logo_senai()
print(f"Soma: {soma}")
print(f"Subtração: {subtração}")
print(f"Multiplicação: {multiplicação}")
print(f"Divisão: {divisão}")
