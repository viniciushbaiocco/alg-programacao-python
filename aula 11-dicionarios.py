# 1. Crie um dicionário vazio
dicionario = {}
# 2. Considerando a chave como sendo nome, e os valores
# idade e cidade. Faça com que 10 elementos sejam
# inseridos via teclado nesse dicionário
for i in range(10):
    nome = input("digite seu nome: ")
    idade = int(input("digite sua idade: "))
    cidade = input("digite sua cidade: ")
    dicionario[nome] = idade,cidade
# 3. Leia um nome e se ele existir no dicionário imprima os o
# nome e a idade
consulta = input("digite um nome para consultar no dicionario: ")
dicionario.get(consulta, "não encontrado")
# 4. Leia um nome e modifique os valores associados a esse
# nome, se ele existir no dicionário
alterar = input("digite a idade que queira alterar no dicionário: ")
alterar2 = input("digite a cidade que queira alterar no dicionário: ")
alvo = input("digite pra qual nome queira trocar: ")
if alvo in dicionario:
    dicionario[alvo] = alterar,alterar2 
else:
    print("nome não encontrado no dicionário")
# 5. Remova um determinado item desse dicionário
remover = input("digite o nome do cadastro que queira remover: ")
if remover in dicionario:
    del dicionario[remover]
else:
    print("nome não encontrado no dicionário")
# 6. Imprima o dicionário
print(dicionario)