# Escreva um programa que receba uma string do
# usuário e a converta para maiúsculas
"""
nome = input("Por favor, digite o seu nome: ")
print(nome.upper())
"""

# Faça um programa que peça ao usuário para digitar
# uma data no formato "dd/mm/aaa" e em seguida imprima
# o dia, o mês e o ano separadamente.
data = input("Digite uma data no formato 'dd/mm/aaaa': ")
dma = data.split("/")
print(f"O dia é: {dma[0]}, o mês é: {dma[1]} e o ano é: {dma[2]}")
print(dma)