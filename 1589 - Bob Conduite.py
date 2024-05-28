""" Você tem em mãos dois cabos circulares de energia. O primeiro cabo tem raio R1 e o segundo raio R2.
Você precisa comprar um conduite circular (veja a imagem abaixo que ilustra um conduite) de maneira a passar os dois cabos por dentro dele:

Qual o menor raio do conduite que você deve comprar? Em outras palavras, dado dois círculos, qual o raio do menor círculo que possa englobar ambos os dois?

Entrada
Na primeira linha teremos um inteiro T (T ≤ 10000), indicando o número de casos de teste.

Na única linha de cada caso teremos dois números inteiros R1 e R2, indicando os respectivos raios. Os inteiros serão positivos e todas as contas caberão em um inteiro normal de 32 bits.

Saída
Em cada caso, imprima o menor raio possível em uma única linha """

testes = int(input(""))

if (testes <= 10000):

    for teste in range(1, testes + 1):

        R1, R2 = str(input("")).split()

        R1 = int(R1)
        R2 = int(R2)

        if (R1 > 0) and (R2 > 0):

            raio_conduite = R1 + R2
        print(raio_conduite)

else:
    print('error')