"""Faça um programa que leia 5 valores inteiros. Conte quantos destes valores digitados são pares e mostre esta informação.

Entrada
O arquivo de entrada contém 5 valores inteiros quaisquer.

Saída
Imprima a mensagem conforme o exemplo fornecido, indicando a quantidade de valores pares lidos."""

listaValores = []
nValoresPares = 0

for i in range(1, 6):
    valor = int(input(""))
    listaValores.append(valor)

pares = len([valor for valor in listaValores if valor % 2 == 0])
print(f"{pares} valores pares")