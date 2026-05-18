# 1. Faça uma pesquisa sobre os métodos remove(), del() e pop(). Para
# que servem, qual a diferença entre eles?

"""Os tres metodos executam uma função em comum, apagar um item da lista, porem a forma que são executados
ou a forma que ele retorna para você, é diferente. 
Del apaga um item da lista, voce pede a remoção pelo indice.
Remove tambem apaga um item da lista, voce pede a remoção pelo proprio valor ao inves de indice.
Pop apaga o item da lista e retorna ele como valor pra voce, voce pede a remoção pelo indice."""

# 2. Implemente os exercícios pedidos na aula Teórica de Listas e de
# Exercícios sobre Listas
# introducao

# def copia_valores(lista):
#     a = (lista[2][1]).copy()
#     return a
# lista = [16, 27, [2, [ 3, 6, 7], 17], 9, 23]
# copiada = copia_valores(lista)
# print(copiada)

# 1

# lista = []
# for i in range (10):
#     valor = int(input("digite o termo inteiro da lista: "))
#     lista.append(valor)
# for i in range(len(lista)):
#     lista[i] = lista [i]*i
# print(lista)

# 2
# def append_lista(lista):
#     for i in range(10):
#         valor = int(input("digite o valor pra lista: "))
#         lista.append(valor)
#     return lista

# lista1 = []
# lista1 = append_lista(lista1)
# lista2 = []
# lista2 = append_lista(lista2)
# lista3 = []

# def comparar_lista(lista,lista2,lista3):
#     for i in lista:
#         if i in lista2:
#             lista3.append(i)
#     return lista3

# comparar_lista(lista1,lista2,lista3)

# print(f"{lista1}\n{lista2}\n{lista3}")

# 3 
# lista1 = []
# lista2 = []
# valor = int(input("digite quantos itens estarão nas duas listas: "))

# def append_listas(lista,valor):
#     for _ in range (valor):
#         elemento = int(input("digite o item da lista: "))
#         lista.append(elemento)

# append_listas(lista1,valor)
# append_listas(lista2,valor)

# lista3 = []

# for i in range(0,len(lista1),2):
#     valor = lista1[i]
#     lista3.append(valor)
# for i in range(0,len(lista2),2):
#     valor = lista2[i]
#     lista3.append(valor)

# print(f"{lista1}\n{lista2}\n{lista3}")

# 4
# alunos = []
# for i in range(10):
#     print(f"Aluno {i + 1}: ")
#     idade = int(input("digite sua idade: "))
#     altura = int(input("digite sua altura: "))
#     alunos.append([idade,altura])

# soma_altura = 0
# for i in alunos:
#     soma_altura += i[1]

# media_altura = soma_altura/10
# contador = 0

# for i in alunos:
#     if i[0] > 20:
#         if i[1] < media_altura:
#             contador += 1

# print(contador)

# 5
# atleta = []
# quantidade = int(input("quantos atletas participaram da competição: "))
# for _ in range (quantidade):
#     nome = input("digite o nome do atleta: ")
#     saltos = []
#     soma_saltos = 0
#     for j in range (5):
#         distancia = float(input(f"digite a distancia {j + 1}: "))
#         soma_saltos += distancia
#         saltos.append(distancia)
#     media_saltos = soma_saltos/5
#     atleta.append([nome, saltos, media_saltos])

# lugar1 = 0
# lugar2 = 0
# lugar3 = 0
# nome1 = ""
# nome2 = ""
# nome3 = ""

# for i in atleta:
#     if i[2] > lugar1:
#         lugar3 = lugar2 
#         nome3 = nome2
#         lugar2 = lugar1
#         nome2 = nome1     
#         lugar1 = i[2]
#         nome1 = i[0]
        
#     elif i[2] > lugar2:
#         lugar3 = lugar2
#         nome3 = nome2
#         lugar2 = i[2] +
#         nome2 = i[0]
        
#     elif i[2] > lugar3:
#         lugar3 = i[2]
#         nome3 = i[0]

# print(f"1º Lugar: {nome1} com média {lugar1:.2f}")
# print(f"2º Lugar: {nome2} com média {lugar2:.2f}")
# print(f"3º Lugar: {nome3} com média {lugar3:.2f}")

# 3. Elabore um programa que leia uma lista de no máximo 20
# elementos inteiros. Em seguida o programa deverá imprimir a
# quantidade de valores múltiplos de 3.

# lista = []
# for i in range(20):
#     valor = int(input("digite o elemento da lista: "))
#     lista.append(valor)
# for i in range(len(lista)):
#     if lista[i] % 3 == 0:
#         print(lista[i])

# 4. Elabore um programa que leia um conjunto de vários valores
# inteiros e os coloque em 2 listas conforme forem pares ou ímpares
# (uma lista para números pares e outra lista para números
# ímpares). A leitura dos números é finalizada quando um número negativo é lido.

# 5. Elabore um programa que leia uma lista de no máximo 10
# elementos reais, o programa deverá imprimir o maior e
# segundo maior elemento e suas respectivas posições na
# lista

# 6. Foram anotadas as idades e alturas de 30 alunos. Faça um
# Programa que determine quantos alunos com mais de 13
# anos possuem altura inferior à média de altura desses
# alunos.
# 7. Construa um programa que leia dois números inteiros: a e b
# e uma lista com N valores inteiros (N fornecido pelo usuário).
# O programa deverá imprimir quantos elementos da Lista
# pertencem ao intervalo [a;b]

# 8. Construa um programa que seja constituído de uma lista
# GAB de 10 elementos caracteres ( esta lista pode ser
# constituída somente dos caracteres a, b, c, d e e. O programa
# irá ler o nome e a resposta de 10 alunos de uma turma e
# deverá imprimir a nota de cada aluno (considerando que
# cada questão vale 1,0 ponto). O programa deverá também
# imprimir a média da sala
# Python

# 9. Utilizando listas faça um programa que faça 5 perguntas para uma
# pessoa sobre um crime. As perguntas são:
# a. "Telefonou para a vítima?"
# b. "Esteve no local do crime?"
# c. "Mora perto da vítima?"
# d. "Devia para a vítima?"
# e. "Já trabalhou com a vítima?"
# O programa deve no final emitir uma classificação sobre a
# participação da pessoa no crime. Se a pessoa responder
# positivamente a 2 questões ela deve ser classificada como
# "Suspeita", entre 3 e 4 como "Cúmplice" e 5 como "Assassino".
# Caso contrário, ele será classificado como "Inocente".