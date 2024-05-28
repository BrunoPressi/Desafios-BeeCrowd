"""Leia 3 valores de ponto flutuante A, B e C e ordene-os em ordem decrescente,
de modo que o lado A representa o maior dos 3 lados.
A seguir, determine o tipo de triângulo que estes três lados formam, com base nos seguintes casos, sempre escrevendo uma mensagem adequada:

se A ≥ B+C, apresente a mensagem: NAO FORMA TRIANGULO
se A2 = B2 + C2, apresente a mensagem: TRIANGULO RETANGULO
se A2 > B2 + C2, apresente a mensagem: TRIANGULO OBTUSANGULO
se A2 < B2 + C2, apresente a mensagem: TRIANGULO ACUTANGULO
se os três lados forem iguais, apresente a mensagem: TRIANGULO EQUILATERO
se apenas dois dos lados forem iguais, apresente a mensagem: TRIANGULO ISOSCELES

Entrada
A entrada contem três valores de ponto flutuante de dupla precisão A (0 < A) , B (0 < B) e C (0 < C).

Saída
Imprima todas as classificações do triângulo especificado na entrada."""
    
valores = str(input(""))
lista_valores = valores.split()

B = float(lista_valores[0])
C = float(lista_valores[1])
A = float(lista_valores[2])

lista_valores.sort()

nova_lista = [A, B, C]
nova_lista.sort(reverse=True)

# nova_lista[0] = A
# nova_lista[1] = B
# nova_lista[2] = C

if nova_lista[0] >= (nova_lista[1] + nova_lista[2]): # se A >= B + C, apresente a mensagem: NAO FORMA TRIANGULO
    print("NAO FORMA TRIANGULO")
else:
    quit
    if nova_lista[0]**2 == (nova_lista[1]**2) + (nova_lista[2]** 2): # se A**2 = B**2 + C**2, apresente a mensagem: TRIANGULO RETANGULO
        print("TRIANGULO RETANGULO")
    if nova_lista[0]**2 > (nova_lista[1]**2) + (nova_lista[2]**2): # se A**2 > B**2 + C**2, apresente a mensagem: TRIANGULO OBTUSANGULO
        print("TRIANGULO OBTUSANGULO")
    if nova_lista[0]**2 < (nova_lista[1]**2) + (nova_lista[2]**2): # se A**2 < B**2 + C**2, apresente a mensagem: TRIANGULO ACUTANGULO
        print("TRIANGULO ACUTANGULO")
    if nova_lista[0] == nova_lista[1] == nova_lista[2]: # se os três lados forem iguais, apresente a mensagem: TRIANGULO EQUILATERO
        print("TRIANGULO EQUILATERO")
    if (nova_lista[0] == nova_lista [1] != nova_lista[2]) or (nova_lista[1] == nova_lista[2] != nova_lista[0]): # se apenas dois dos lados forem iguais, apresente a mensagem: TRIANGULO ISOSCELES
        print("TRIANGULO ISOSCELES")
