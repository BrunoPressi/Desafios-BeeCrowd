"""Escreva um algoritmo que leia 2 valores inteiros X e Y calcule a soma dos números que não são múltiplos de 13 entre X e Y, incluindo ambos.

Entrada
O arquivo de entrada contém 2 valores inteiros quaisquer, não necessariamente em ordem crescente.

Saída
Imprima a soma de todos os valores não divisíveis por 13 entre os dois valores lidos na entrada, inclusive ambos se for o caso."""

x = int(input(""))
y = int(input(""))

listaNumsNaoMultiplos = []
somaNaoMultiplos = 0

if x < y:
    for i in range(x, y + 1):
        if (i % 13 > 0):
            listaNumsNaoMultiplos.append(i)

if x > y:
    for i in range(y, x + 1):
        if (i % 13 > 0):
            listaNumsNaoMultiplos.append(i)

for i in listaNumsNaoMultiplos:
    somaNaoMultiplos += i
print(somaNaoMultiplos)