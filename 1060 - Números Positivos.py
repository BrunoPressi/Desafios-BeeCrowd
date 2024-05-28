"""Faça um programa que leia 6 valores. Estes valores serão somente negativos ou positivos (desconsidere os valores nulos). A seguir, mostre a quantidade de valores positivos digitados.

Entrada
Seis valores, negativos e/ou positivos.

Saída
Imprima uma mensagem dizendo quantos valores positivos foram lidos."""

listaValores = []

for i in range(1, 7):
    valor = float(input(""))
    listaValores.append(valor)
    valoresPositivos = [valor for valor in listaValores if valor > 0]
print("{} valores positivos".format(len(valoresPositivos)))