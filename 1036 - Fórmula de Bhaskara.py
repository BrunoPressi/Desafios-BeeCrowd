"""Leia 3 valores de ponto flutuante e efetue o cálculo das raízes da equação de Bhaskara.
Se não for possível calcular as raízes, mostre a mensagem correspondente “Impossivel calcular”,
caso haja uma divisão por 0 ou raiz de numero negativo.

Entrada
Leia três valores de ponto flutuante (double) A, B e C.

Saída
Se não houver possibilidade de calcular as raízes, apresente a mensagem "Impossivel calcular".
Caso contrário, imprima o resultado das raízes com 5 dígitos após o ponto,
com uma mensagem correspondente conforme exemplo abaixo. Imprima sempre o final de linha após cada mensagem."""

import math

# valores precisam ser maiores que 0
valores = str(input("")) 
lista_valores = valores.split(" ")

a = float(lista_valores[0])
b = float(lista_valores[1])
c = float(lista_valores[2])

delta = (b**2) - (4 * a * c)

if (a > 0) & (b > 0) & (c > 0) & (delta > 0):
    raiz = math.sqrt(delta)
    R1 = (-b + raiz) / (2 * a)
    R2 = (-b - raiz) / (2 * a)
    txt = "R1 = {:.5f}\nR2 = {:.5f}"
    print(txt.format(R1, R2))
else:
    print("Impossivel calcular")
