"""Leia 2 valores inteiros X e Y. A seguir, calcule e mostre a soma dos números impares entre eles.

Entrada
O arquivo de entrada contém dois valores inteiros.

Saída
O programa deve imprimir um valor inteiro.
Este valor é a soma dos valores ímpares que estão entre os valores fornecidos na entrada que deverá caber em um inteiro."""

x = int(input(""))
y = int(input(""))

somaImpares = 0

if (x > y):

    for numero in range(y + 1, x):
        if (numero % 2 > 0) or (numero % 2 < 0):
            somaImpares += numero
    print(somaImpares)

elif (y > x):
    for numero in range(x + 1, y):
        if (numero % 2 > 0) or (numero % 2 < 0 ):
            somaImpares += numero
    print(somaImpares)
