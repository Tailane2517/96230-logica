import os
os.system("cls || clear")

#Criando uma lista
lista_notas = []

#Adicionando 3 notas em uma lista.
for i in range(3):
    nota = float(input("Digite uma nota: "))
    lista_notas.append(nota)
#append significar colocar a nota na lista

#Soma
soma = sum(lista_notas)


#Exibindo todos os valores em uma lista.
print()
for nota in lista_notas: #ForEach: é um for que não diz quantas vezes vai repetir,ele descobre a quantidade de elementos
    print(nota)