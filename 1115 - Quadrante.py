"""Escreva um programa para ler as coordenadas (X,Y) de uma quantidade indeterminada de pontos no sistema cartesiano.
Para cada ponto escrever o quadrante a que ele pertence.
O algoritmo será encerrado quando pelo menos uma de duas coordenadas for NULA (nesta situação sem escrever mensagem alguma).

Entrada
A entrada contém vários casos de teste. Cada caso de teste contém 2 valores inteiros.

Saída
Para cada caso de teste mostre em qual quadrante do sistema cartesiano se encontra a coordenada lida, conforme o exemplo."""

while True:
    X, Y = (str(input("")).split())

    # faço a conversão dos valores nas váriaveis X e Y para números inteiros.
    X = int(X)
    Y = int(Y)

    # condição de parada do loop.
    if X == 0 or Y == 0:
        exit()
    
    # condições de verificação dos quadrantes das minhas coordenadas X e Y.
    elif X > 0 and Y > 0: print("primeiro")
    elif X < 0 and Y > 0: print("segundo")
    elif X < 0 and Y < 0: print("terceiro")
    elif X > 0 and Y < 0: print("quarto")
        