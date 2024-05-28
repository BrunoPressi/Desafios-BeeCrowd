"""Leia 4 valores inteiros A, B, C e D. A seguir, se B for maior do que C e se D for maior do que A,
e a soma de C com D for maior que a soma de A e B e se C e D, ambos, forem positivos e se a variável
A for par escrever a mensagem "Valores aceitos", senão escrever "Valores nao aceitos".

Entrada
Quatro números inteiros A, B, C e D.

Saída
Mostre a respectiva mensagem após a validação dos valores."""

valores = str(input(""))
lista_valores = valores.split(" ")

A = int(lista_valores[0]) # precisa ser par
B = int(lista_valores[1])
C = int(lista_valores[2]) # precisa ser positivo
D = int(lista_valores[3]) # precisa ser positivo 

soma_CD = C + D
soma_AB = A + B


if (B > C) & (D > A) & (soma_CD > soma_AB) & (C > 0) & (D > 0) & (A % 2 == 0):
    print("Valores aceitos")
else:
    print("Valores nao aceitos")
