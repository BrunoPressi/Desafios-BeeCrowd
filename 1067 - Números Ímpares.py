"""Leia um valor inteiro X (1 <= X <= 1000). Em seguida mostre os ímpares de 1 até X, um valor por linha, inclusive o X, se for o caso.

Entrada
O arquivo de entrada contém 1 valor inteiro qualquer.

Saída
Imprima todos os valores ímpares de 1 até X, inclusive X, se for o caso."""

valor = int(input(""))
listaI = []

for i in range(1, valor + 1):
    listaI.append(i)

impares = [i for i in listaI if i % 2 > 0]

for x in impares:
    print(x)