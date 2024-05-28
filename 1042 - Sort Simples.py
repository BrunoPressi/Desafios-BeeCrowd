"""Leia 3 valores inteiros e ordene-os em ordem crescente.
No final, mostre os valores em ordem crescente, uma linha em branco e em seguida, os valores na sequência como foram lidos.

Entrada
A entrada contem três números inteiros.

Saída
Imprima a saída conforme foi especificado."""

valores = str(input(""))

lista_valores = valores.split()

valor1 = int(lista_valores[0])
valor2 = int(lista_valores[1])
valor3 = int(lista_valores[2])

nova_lista = [valor1, valor2, valor3]
nova_lista.sort()

print(nova_lista[0])
print(nova_lista[1])
print(nova_lista[2])
print("")
print(lista_valores[0])
print(lista_valores[1])
print(lista_valores[2])
