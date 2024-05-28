"""Leia 5 valores Inteiros. A seguir mostre quantos valores digitados foram pares,
quantos valores digitados foram ímpares, quantos valores digitados foram positivos e quantos valores digitados foram negativos.

Entrada
O arquivo de entrada contém 5 valores inteiros quaisquer.

Saída
Imprima a mensagem conforme o exemplo fornecido, uma mensagem por linha, não esquecendo o final de linha após cada uma."""

listaValores = []

for i in range (1, 6):
    valor = int(input(""))
    listaValores.append(valor)

pares = len([valor for valor in listaValores if valor % 2 == 0])
impares = len([valor for valor in listaValores if valor % 2 > 0])
positivos = len([valor for valor in listaValores if valor > 0])
negativos = len([valor for valor in listaValores if valor < 0])

print(f"{pares} valor(es) par(es)")
print(f"{impares} valor(es) impar(es)")
print(f"{positivos} valor(es) positivo(s)")
print(f"{negativos} valor(es) negativo(s)")