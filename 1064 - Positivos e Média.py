"""Leia 6 valores. Em seguida, mostre quantos destes valores digitados foram positivos.
Na próxima linha, deve-se mostrar a média de todos os valores positivos digitados, com um dígito após o ponto decimal.

Entrada
A entrada contém 6 números que podem ser valores inteiros ou de ponto flutuante. Pelo menos um destes números será positivo.

Saída
O primeiro valor de saída é a quantidade de valores positivos. A próxima linha deve mostrar a média dos valores positivos digitados."""

lista_valores = []
lista_valores_num = []
soma_positivos = 0

for i in range(1, 7):
    n = str(input(""))
    lista_valores.append(n)
for item in lista_valores:
    lista_valores_num.append(float(item))
    positivos = [n for n in lista_valores_num if n > 0]
for x in positivos:
    soma_positivos += x
print(f"{len(positivos)} valores positivos")
txt = "{:.1f}"
print(txt.format(soma_positivos / len(positivos)))
