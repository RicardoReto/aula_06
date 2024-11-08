# Crie um script que solicite ao usuário uma lista de números separados por
# vírgula. O programa deve converter a string de entrada em uma lista de
# números inteiros. Utilize try-except para tratar a conversão de cada nú-
# mero e validar que cada elemento da lista convertida é um inteiro. Se a
# conversão falhar ou um elemento não for um inteiro, imprima uma mensagem
# de erro. Se a conversão for bem-sucedida para todos os elementos, imprima
# uma lista de inteiros.

lista = input("Digite uma lista de números inteiros separados por vírgula: ")
lista = lista.split(',')
certo = [None for x in range(len(lista))]

for n in range(len(lista)):
    try:
        certo[n] = isinstance(int(lista[n]), int)
    except:
        print(f"O valor {lista[n]} não é um inteiro")
if all(certo):
    print("Todos os números digitados são inteiros:")
    print(lista)