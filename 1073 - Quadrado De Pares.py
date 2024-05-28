"""Leia um valor inteiro N. Apresente o quadrado de cada um dos valores pares, de 1 até N, inclusive N, se for o caso.

Entrada
A entrada contém um valor inteiro N (5 < N < 2000).

Saída
Imprima o quadrado de cada um dos valores pares, de 1 até N, conforme o exemplo abaixo."""

N = int(input(""))
listaValoresAteN = []

for i in range(1, N + 1):
    listaValoresAteN.append(i)

pares = [i for i in listaValoresAteN if i % 2 == 0]

for i in pares:
    quadrado = i ** 2
    print(f"{i}^2 = {quadrado}")