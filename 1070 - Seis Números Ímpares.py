"""Leia um valor inteiro X. Em seguida apresente os 6 valores ímpares consecutivos a partir de X,
um valor por linha, inclusive o X ser for o caso.

Entrada
A entrada será um valor inteiro positivo.

Saída
A saída será uma sequência de seis números ímpares."""

listaNumeros = []
valor = int(input(""))

for i in range(valor * 3):
    listaNumeros.append(i)

impares = ([i for i in listaNumeros if (i % 2 > 0) and (i >= valor)])
print(impares[0])
print(impares[1])
print(impares[2])
print(impares[3])
print(impares[4])
print(impares[5])