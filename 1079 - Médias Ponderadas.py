"""Leia 1 valor inteiro N, que representa o número de casos de teste que vem a seguir.
Cada caso de teste consiste de 3 valores reais, cada um deles com uma casa decimal.
Apresente a média ponderada para cada um destes conjuntos de 3 valores,
sendo que o primeiro valor tem peso 2, o segundo valor tem peso 3 e o terceiro valor tem peso 5.

Entrada
O arquivo de entrada contém um valor inteiro N na primeira linha.
Cada N linha a seguir contém um caso de teste com três valores com uma casa decimal cada valor.

Saída
Para cada caso de teste, imprima a média ponderada dos 3 valores, conforme exemplo abaixo."""

N = int(input(""))
listaValores = []

for i in range(N):
    valores = str(input("")) 

    # armazena os valores em uma lista.
    listaValores = valores.split()

    # converte cada valor da lista para float.
    valor1 = float(listaValores[0])
    valor2 = float(listaValores[1])
    valor3 = float(listaValores[2])

    # calcule da média ponderada, conforme enunciado.
    media = ((valor1 * 2) + (valor2 * 3) + (valor3 * 5)) / 10
    print("{:.1f}".format(media))