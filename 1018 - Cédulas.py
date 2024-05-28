"""Leia um valor inteiro. A seguir, calcule o menor número de notas possíveis (cédulas) no qual o valor pode ser decomposto.
As notas consideradas são de 100, 50, 20, 10, 5, 2 e 1. A seguir mostre o valor lido e a relação de notas necessárias.

Entrada
O arquivo de entrada contém um valor inteiro N (0 < N < 1000000).

Saída
Imprima o valor lido e, em seguida, a quantidade mínima de notas de cada tipo necessárias, conforme o exemplo fornecido.
Não esqueça de imprimir o fim de linha após cada linha, caso contrário seu programa apresentará a mensagem: “Presentation Error”."""

dinheiro = int(input(""))

notas_100 = (dinheiro // 100)
resto_notas_100 = (dinheiro - (notas_100 * 100))

notas_50 = (resto_notas_100 // 50)
resto_notas_50 = (resto_notas_100 - (notas_50 * 50))

notas_20 = (resto_notas_50 // 20)
resto_notas_20 = (resto_notas_50 - (notas_20 * 20))

notas_10 = (resto_notas_20 // 10)
resto_notas_10 = (resto_notas_20 - (notas_10 * 10))

notas_5 = (resto_notas_10 // 5)
resto_notas_5 = (resto_notas_10 - (notas_5 * 5))

notas_2 = (resto_notas_5 // 2)
resto_notas_2 = (resto_notas_5 - (notas_2 * 2))

notas_1 = (resto_notas_2 // 1)
resto_notas_1 = (resto_notas_2 - (notas_1))

print(dinheiro)
print(f"{notas_100} nota(s) de R$ 100,00")
print(f"{notas_50} nota(s) de R$ 50,00")
print(f"{notas_20} nota(s) de R$ 20,00")
print(f"{notas_10} nota(s) de R$ 10,00")
print(f"{notas_5} nota(s) de R$ 5,00")
print(f"{notas_2} nota(s) de R$ 2,00")
print(f"{notas_1} nota(s) de R$ 1,00")