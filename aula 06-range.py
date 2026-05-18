# # exercicio 1: somar os numeros de 1 até n
# soma = 0
# n=int(input("qtde: "))
# for i in range (1,n + 1):
#     soma += i
#     print(soma)

# # exercicio 2: somar os numeros pares de 1 até n
# N = int(input("digite qtde: "))
# soma = 0 
# for i in range (1,N+1):
#     if i % 2 == 0:
#         soma +=i
#         print(soma)

# # exercicio 3: exercicio ainda sem resolucao no arquivo

# # exercicio 4: exercicio ainda sem resolucao no arquivo

# # exercicio 5: contar quantos numeros caem em cada faixa de intervalo
# i = int(input("qts numeros: "))
# c1=0
# c2=0
# c3=0
# c4=0
# while i>0:
#     num = int(input("digite o(s) numero(s): "))
#     i -= 1
#     if num <= 25: 
#         c1 += 1
#     elif num <= 50:
#         c2 =+ 1
#     elif num <= 75:
#         c3 += 1
#     elif num <= 100:
#         c4 += 1
# print (f"<25 = {c1}, <50 = {c2}, <75 = {c3}, <100 = {c4}")

# # exercicio 6: exibir multiplos de 4 menores que n
# n = int(input("numero: "))
# for i in range (1, n):
#     if i % 4 == 0:
#         print(i)

# # exercicio 7: encontrar os dois maiores numeros de uma sequencia
# c=1
# n=int(input("digite o numero: "))
# m1=n
# m2=n-1
# while c<10:
#     n=int(input("digite o numero: "))
#     c += 1
#     if n>m1:
#         m2 = m1
#         m1 = n
#     else:
#         if n>m2:
#             m2 = n
# print(f"{m1},{m2}")

# # exercicio 8: converter temperaturas de Fahrenheit para Celsius
# f = 28
# for i in range (f,51, +2):
#     c = (i-32)/1.8
#     print(f"Fahrenheit: {i:.1f}")
#     print(f"Celsius: {c:.1f}")

# # exercicio 9: calcular a soma de uma serie com numeros impares
# soma = 0
# for i in range(1, 51):
#     nm= 2*i-1
#     r= nm/i
#     soma += r
# print(f"{soma}")

# # exercicio 10: calcular a soma de uma serie fracionaria
# soma = 0
# nm = 1
# for i in range(3, 42, 2):
#     r = nm / i
#     soma += r
#     nm += 1
# print(f"resultado = {soma:.3f}")

# # exercicio 11: calcular medias e contar pares e impares
# qtpares = 0
# qttotal = 0
# pares = 0
# impares = 0
# total = 0
# i = int(input("quantos numeros: "))
# for i in range (i):
#     n = int(input("digite numeros positivos inteiros: "))
#     if n < 0:
#         print("tem que ser um numero inteiro")
#     else: 
#         if n%2 == 0:
#             qtpares += 1
#             pares += n
#         else:
#             if n%2 == 1:
#                 impares += 1 
#     total += n
#     qttotal += 1
# media= total/qttotal
# media_pares = pares/qtpares
# print(f"A media total é {media} | A media dos pares é {media_pares} | Temos {qtpares} pares e {impares} numeros impares")

# # exercicio 12: gerar termos de uma sequencia e somar os valores
# i = int(input("digite a sequencia: "))
# inicial = 2
# inicial2 = 3
# soma = 0
# for i in range(i):
#     soma += inicial
#     proximo = inicial + inicial2
#     inicial = inicial2
#     inicial2 = proximo
#     print(f"a ={inicial}|b= {inicial2}|proximo item= {proximo}")
# print(soma) 

# # exercicio 13: calcular estatisticas de salario e filhos dos habitantes
# habitantes = int(input("numero de habitantes: "))
# maiorsalario = 0
# abaixode100 = 0
# mediasalario = 0
# mediafilhos = 0
# abaixode100final= 0
# for _ in range (habitantes):
#     salario = int(input("seu salario: "))
#     filhos = int(input("numero de filhos: "))
#     mediasalario += salario
#     mediafilhos += filhos
#     if salario > maiorsalario:
#         maiorsalario = salario
#     if salario < 100:
#         abaixode100 += 1
# mediafinalsalario= mediasalario/habitantes
# mediafinalfilhos= mediafilhos/habitantes
# if abaixode100 != 0:
#     abaixode100final= (abaixode100/habitantes)*100
# print(f"salario medio: {mediafinalsalario} | maior salario: {maiorsalario} | qtde. media de filhos {mediafinalfilhos} | percentual abaixo de 100: {abaixode100final}%")

# # exercicio 14: calcular o fatorial de varios numeros
# qtde = int(input("quantos numeros?: "))
# fatorial = 1
# for _ in range (qtde):
#     numero = int(input("numero: "))
#     if numero < 0:
#         print("não pode ter um numero negativo")
#     else:
#         for _ in range (numero):
#             fatorial *= numero
#             numero -= 1
#             print(fatorial)
#         fatorial = 1

# # exercicio 15: analisar idade, altura e peso de um grupo de pessoas
# idade50=0
# qtde10e20=0
# num10e20=0
# pesomenor50=0
# for i in range (1, 26):
#     idade=int(input("digite sua idade: "))
#     altura=int(input("digite sua altura: "))
#     peso=int(input("digite seu peso: "))
#     if idade>50:
#         idade50 += 1
#     if 10<idade<20:
#         qtde10e20 += altura
#         num10e20 += 1
#     if peso<50:
#         pesomenor50 += 1
# if num10e20>0:
#     media10e20=qtde10e20/num10e20
# else:
#     media10e20=0
# percentual50=(pesomenor50/5)*100
# print(f"idade > 50 {idade50} | media de 10 e 20: {media10e20} | percentual de peso menor que 50: {percentual50} ")

## exercicio 16: verificar se um numero é primo pelo total de divisores
# numerosdivisores = 0
# num = int(input("digite o numero: "))
# for div in range (1,num+1):
#     if num % div == 0:
#         numerosdivisores += 1
# if numerosdivisores == 2:
#     print("primo")
# else:
#     print("não é primo")
