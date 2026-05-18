## exercicio 1: retornar o antecessor e o sucessor de um numero
# def anterior_sucessor (numero):
#     anterior = numero - 1
#     sucessor = numero + 1
#     return anterior, sucessor
# numero = int(input("numero: "))
# anterior, sucessor = anterior_sucessor(numero)
# print(f"anterior: {anterior}")
# print(f"sucessor: {sucessor}")

## exercicio 2: somar tres numeros e exibir o resultado com uma funcao auxiliar
# def ler (numero):
#     print (numero)
# def soma (n1, n2, n3):
#     soma = 0
#     soma = n1 + n2 + n3
#     return soma
# soma = soma (10, 20, 30)
# ler(soma)
# soma()

## exercicio 3: calcular o custo final de um item com imposto
# def soma_Imposto (taxaImposto, custo):
#     imposto = custo * (taxaImposto/100)
#     custo_final = custo + imposto
#     return custo_final
# taxa = float(input("digite a taxa: "))
# custo = float(input("digite o custo: "))
# valor_final = soma_Imposto(taxa, custo)
# print(f"valor final + imposto = {valor_final}")

## exercicio 4: mostrar os numeros pares entre dois valores
# def valores (a,b):
#     if a>b:
#         for i in range (b,a):
#             if i%2 == 0:
#                 print(i)
#     else:
#         for i in range (a,b):
#             if i%2 == 0:
#                 print(i)
# a = int(input("digite valor a: "))
# b = int(input("digite valor b: "))
# valores(a,b)

## exercicio 5: calcular o fatorial de tres numeros separadamente
# def fatorial(numero):
#     fatorial = numero 
#     for i in range (2, numero):
#         fatorial *= i
#     return fatorial
# n1 = int(input("Digite o primeiro número: "))
# n2 = int(input("Digite o segundo número: "))
# n3 = int(input("Digite o terceiro número: "))
# print(fatorial(n1))
# print(fatorial(n2))
# print(fatorial(n3))

## exercicio 6: somar os digitos e encontrar o maior digito de um numero
# def soma_digitos(numero):
#     soma = 0
#     while numero > 0:
#         digitos = numero % 10
#         numero = numero // 10
#         soma += digitos
#     print(soma)
#     return soma
# def maior_digito(numero):
#     check = 0
#     while numero > 0:
#         digitos = numero % 10
#         numero = numero // 10
#         if digitos > check:
#             check = digitos
#     print(check)
#     return check
# numero = int(input("numero aqui: "))
# soma_digitos(numero)
# maior_digito(numero)

## exercicio 7: verificar se um numero é perfeito
# def perfeito(numero):
#     soma = 0
#     for i in range (1,numero):
#         if numero % i == 0:
#             soma += i
#     if soma == numero:
#         print("é perfeito")
#     else:
#         print("não é perfeito")
# numero = int(input("numero: "))
# perfeito(numero)
