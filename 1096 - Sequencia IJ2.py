"""Você deve fazer um programa que apresente a sequencia conforme o exemplo abaixo.

Entrada
Não há nenhuma entrada neste problema.

Saída
Imprima a sequencia conforme exemplo abaixo

I=1 J=7
I=1 J=6
I=1 J=5
I=3 J=7
I=3 J=6
I=3 J=5
...
I=9 J=7
I=9 J=6
I=9 J=5 """

listaJ = [7, 6, 5]
listaI = [1, 3, 5, 7, 9]

for I in listaI:
    for J in listaJ:
        print(f"I={I} J={J}")