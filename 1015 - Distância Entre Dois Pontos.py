"""Leia os quatro valores correspondentes aos eixos x e y de dois pontos quaisquer no plano, p1(x1,y1) e p2(x2,y2)
e calcule a distância entre eles, mostrando 4 casas decimais após a vírgula, segundo a fórmula:

Distancia = (x2 - x1)**2 + (y2 - y1)**2 (Tudo isso em uma raiz quadrada)

Entrada
O arquivo de entrada contém duas linhas de dados. A primeira linha contém dois valores de ponto flutuante:
x1 y1 e a segunda linha contém dois valores de ponto flutuante x2 y2.

Saída
Calcule e imprima o valor da distância segundo a fórmula fornecida, com 4 casas após o ponto decimal."""

import math

p1 = str(input(""))
p2 = str(input(""))

lista_P1 = p1.split()
lista_P2 = p2.split()

x1 = float(lista_P1[0])
y1 = float(lista_P1[1])

x2 = float(lista_P2[0])
y2 = float(lista_P2[1])

distancia = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

txt = "{:.4f}"
print(txt.format(distancia))