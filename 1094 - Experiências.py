"""Maria acabou de iniciar seu curso de graduação na faculdade de medicina e precisa de sua ajuda para organizar os experimentos
de um laboratório o qual ela é responsável. Ela quer saber no final do ano, quantas cobaias foram utilizadas no laboratório
e o percentual de cada tipo de cobaia utilizada.

Este laboratório em especial utiliza três tipos de cobaias: sapos, ratos e coelhos.
Para obter estas informações, ela sabe exatamente o número de experimentos que foram realizados,
o tipo de cobaia utilizada e a quantidade de cobaias utilizadas em cada experimento.

Entrada
A primeira linha de entrada contém um valor inteiro N que indica os vários casos de teste que vem a seguir.
Cada caso de teste contém um inteiro Quantia (1 ≤ Quantia ≤ 15) que representa a quantidade de cobaias utilizadas e um caractere Tipo ('C', 'R' ou 'S'), indicando o tipo de cobaia (R:Rato S:Sapo C:Coelho).

Saída
Apresente o total de cobaias utilizadas, o total de cada tipo de cobaia utilizada e o percentual
de cada uma em relação ao total de cobaias utilizadas, sendo que o percentual deve ser apresentado com dois dígitos após o ponto."""


N_testes = int(input(""))

# variaveis para as cobaias totais e separadas, incialmente 0.
somaCobaiasTotal = 0
somaCobaiasC = 0
somaCobaiasR = 0
somaCobaiasS = 0

for i in range(1, N_testes + 1):
    casoTeste = str(input(""))

    # armazena cada iteração em uma lista de dois índices.
    listaCasoTeste = casoTeste.split()

    # converte o primeiro índice de cada lista para inteiro.
    nCobaias = int(listaCasoTeste[0])

    # calcula o total de cobaias utilizadas no caso teste.
    somaCobaiasTotal += nCobaias

    # condição para verificar se o segundo índice da minha lista de casos teste é "C".
    if listaCasoTeste[1] == "C":

        # caso seja, armazenar o respectivo caso teste em uma nova nova lista: lista coelhos.
        listaCoelhos = casoTeste.split()

        # váriavel para realizar a soma do primeiro índice da minha lista coelhos.
        nCobaiasC = int(listaCoelhos[0])

        # realiza a soma total do número de coelhos usados no caso teste.
        somaCobaiasC += nCobaiasC

    # refazer o passo a passo acima para o restante dos tipos de cobaias.
    if listaCasoTeste[1] == "R":
        listaRatos = casoTeste.split()
        nCobaiasR = int(listaRatos[0])
        somaCobaiasR += nCobaiasR

    # refazer o passo a passo acima para o restante dos tipos de cobaias.
    if listaCasoTeste[1] == "S":
        listaSapos = casoTeste.split()
        nCobaiasS = int(listaSapos[0])
        somaCobaiasS += nCobaiasS

    # calcula o percentual de coelhos em relação ao número total de cobaias.
    percentualCoelhos =  (somaCobaiasC * 100) / somaCobaiasTotal
    txt1 = "Percentual de coelhos: {:.2f} %"

    # calcula o percentual de Ratos em relação ao número total de cobaias.
    percentualRatos = (somaCobaiasR * 100) / somaCobaiasTotal
    txt2 = "Percentual de ratos: {:.2f} %"

    # calcula o percentual de Sapos em relação ao número total de cobaias.

    percentualSapos = (somaCobaiasS * 100) / somaCobaiasTotal
    txt3 = "Percentual de sapos: {:.2f} %"

# saída final:
print(f"Total: {somaCobaiasTotal} cobaias")
print(f"Total de coelhos: {somaCobaiasC}")
print(f"Total de ratos: {somaCobaiasR}")
print(f"Total de sapos: {somaCobaiasS}")
print(txt1.format(percentualCoelhos))
print(txt2.format(percentualRatos))
print(txt3.format(percentualSapos))