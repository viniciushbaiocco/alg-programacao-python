# 1. Faça um programa que solicite o nome do usuário e
# imprima-o na vertical.
nome = input("digite seu nome: ")
for i in range (len(nome)):
    print(nome[i])
# 2. Faça um programa que leia um nome e imprima as 4
# primeiras letras do nome.
nome = input("digite seu nome: ")
print(nome[:4])
# 3. Elabore um programa que leia nome, sexo e idade de um
# usuário. Se sexo for feminino e idade menor que 25,
# imprime o nome da pessoa e a palavra “ACEITA”, caso
# contrário imprimir “NÃO ACEITA”.
nome = input("digite seu nome: ")
sexo = input("qual seu sexo: ")
idade = int(input("qual sua idade: "))
if sexo == "Feminino" and idade < 25:
    print(nome + " " + "ACEITA")
else:
    print("NÃO ACEITA")
# 4. Construa um programa que leia duas strings fornecidas pelo
# usuário e verifique se a segunda string lida está contida no
# final da primeira, imprimindo o resultado da verificação, caso
# a segunda string for maior que a primeira, faça o inverso.
string1 = input("digite a primeira string: ")
string2 = input("digite a segunda string: ")
contido = True
if len(string1) > len(string2):
    tamanho = len(string1) - len(string2)
    for i in range (len(string2)):
        if string1[tamanho + i] != string2[i]:
            contido = False
            break
else:
    tamanho = len(string2) - len(string1)
    for i in range (len(string1)):
        if string2[tamanho + i] != string1[i]:
            contido = False
            break
if contido == True and len(string1) > len(string2):
    print(f"A string {string2} está contida no final da {string1}")
elif contido == True and len(string1) < len(string2):
    print(f"A string {string1} está contida no final da string {string2}")
else:
    print("Não está contido, nem o final da 2 na 1, nem o final da 1 no da 2")
# 5. Escreva um programa que leia a idade e o primeiro nome de
# várias pessoas. Seu programa deve terminar quando uma
# idade negativa for digitada. Ao terminar, seu programa deve
# escrever o nome e a idade da pessoa mais jovem e mais velha.
idade = int(input("digite sua idade aqui: "))
nome = input("digite seu nome aqui: ")
velha = idade
jovem = idade
nome_jovem = nome
nome_velha = nome
while idade >= 0:
    idade = int(input("digite sua idade aqui: "))
    if idade >= 0:
        nome = input("digite seu nome aqui: ")
        if idade < jovem:
            jovem = idade
            nome_jovem = nome
        if idade > velha:
            velha = idade
            nome_velha = nome
print(f"pessoa jovem | nome: {nome_jovem} | idade: {jovem}\npessoa velha | nome: {nome_velha} | idade: {velha}")


# DESAFIO!!! Faça um programa que, dada uma string, diga se ela
# e um palíndromo ou não. Lembrando que um palíndromo e
# uma palavra que tenha a propriedade de poder ser lida tanto
# da direita para a esquerda como da esquerda para a direita.
# • Exemplo:
# • ovo
# • arara
# • Anotaram a data da maratona
reversa = ""
palindromo = True
string = input("digite a string: ")
string = string.replace(" ", "")
string = string.lower()
for i in range (len(string)-1, -1, -1):
    reversa += string[i]
for i in range(len(string)):
    if reversa[i] != string[i]:
        palindromo = False
        break
if palindromo == True:
    print(f"A string {string} é um palindromo")
else:
    print(f"A string {string} não é um palindromo")
