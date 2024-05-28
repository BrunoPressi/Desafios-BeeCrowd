"""Leia um conjunto não determinado de pares de valores M e N (parar quando algum dos valores for menor ou igual a zero).
Para cada par lido, mostre a sequência do menor até o maior e a soma dos inteiros consecutivos entre eles (incluindo o N e M).

Entrada
O arquivo de entrada contém um número não determinado de valores M e N. A última linha de entrada vai conter um número nulo ou negativo.

Saída
Para cada dupla de valores, imprima a sequência do menor até o maior e a soma deles, conforme exemplo abaixo."""

def sequencia_soma():

    while True:

        M, N = str(input()).split()

        M = int(M)
        N = int(N)

        soma = 0
        nums = []

        if (M > 0) and (N > 0):

            if M > N:

                for i in range(N, M + 1):
                    soma += i
                    nums.append(i)
            
                nums = " ".join(map(str,nums))
                txt = (f"{nums} Sum={soma}")

                print(txt)

            elif N > M:

                for i in range(M, N + 1):
                    soma += i
                    nums.append(i)

                nums = " ".join(map(str, nums))
                txt = (f"{nums} Sum={soma}")

                print(txt)

        else:
            return "números precisam ser maiores que zero"
        break

print(sequencia_soma())