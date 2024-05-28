"""Leia 100 valores inteiros. Apresente então o maior valor lido e a posição dentre os 100 valores lidos.

Entrada
O arquivo de entrada contém 100 números inteiros, positivos e distintos.

Saída
Apresente o maior valor lido e a posição de entrada, conforme exemplo abaixo."""

listaValores = []
maiorValor = 0

for i in range(1, 101):
    num = int(input(""))
    listaValores.append(num)

    # condição para verificar o maior valor do range.
    if num > maiorValor:
        maiorValor = num

    # condição para verificar a posição do maior valor do range.
    posicaoMaiorValor = listaValores.index(maiorValor)
print(maiorValor)
print(posicaoMaiorValor + 1)