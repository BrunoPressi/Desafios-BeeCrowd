"""Leia 3 valores reais (A, B e C) e verifique se eles formam ou não um triângulo.
Em caso positivo, calcule o perímetro do triângulo e apresente a mensagem:

Perimetro = XX.X

Em caso negativo, calcule a área do trapézio que tem A e B como base e C como altura, mostrando a mensagem

Area = XX.X

Entrada
A entrada contém três valores reais.

Saída
O resultado deve ser apresentado com uma casa decimal."""

valores = str(input(""))

lista_valores = valores.split()

A = float(lista_valores[0])
B = float(lista_valores[1])
C = float(lista_valores[2])

# Para 3 valores formarem um triângulo, a soma de dois lados deles devem ser maior que o terceiro lado.
if ((A + B) > C) & ((A + C) > B) & ((B + C) > A): 
    perimetro = A + B + C # perimeto = soma dos lados
    print("Perimetro = {:.1f}".format(perimetro))
else:
    area_trapezio = ((A + B) * C) / 2 # area do trapezio = ((base1 + base2) * Altura) / 2
    print("Area = {:.1f}".format(area_trapezio))