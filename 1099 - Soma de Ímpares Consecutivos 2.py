""" Leia um valor inteiro N que é a quantidade de casos de teste que vem a seguir. Cada caso de teste consiste de dois inteiros X e Y.
Você deve apresentar a soma de todos os ímpares existentes entre X e Y.

Entrada
A primeira linha de entrada é um inteiro N que é a quantidade de casos de teste que vem a seguir.
Cada caso de teste consiste em uma linha contendo dois inteiros X e Y.

Saída
Imprima a soma de todos valores ímpares entre X e Y. """

nCasosTestes = int(input(""))

for testes in range(1, nCasosTestes + 1):

    x, y = str(input("")).split()

    soma = 0

    x = int(x)
    y = int(y)

    if (x > y):

        for numeros in range(y + 1, x):
            if (numeros % 2 > 0) or (numeros % 2 < 0):
                soma += numeros
        print(soma)
    
    elif (y > x):

        for numeros in range (x + 1, y):
            if (numeros % 2 > 0) or (numeros % 2 < 0):
                soma += numeros
        print(soma)

    else:
        print("0")