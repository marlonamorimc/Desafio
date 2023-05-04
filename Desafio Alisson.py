'''Desafio Alisson - Pra Amanhã (04 - 05 - 2023)
Como Fazer para contar a quantidade de números pares entre dois números quaisquer?
'''
num1 = int(input("Digite o primeiro número: "))
num2 = int(input("Digite o segundo número: "))

if num1 < num2:
    menor = num1
    maior = num2
else:
    menor = num2
    maior = num1

contador_pares = 0
i = menor

while i <= maior:
    if i % 2 == 0:
        contador_pares += 1
    i += 1

print("Existem", contador_pares, "números pares entre", num1, "e", num2)