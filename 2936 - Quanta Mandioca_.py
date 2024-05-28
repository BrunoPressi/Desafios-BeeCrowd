# crio uma lista para separar a quantidade que cada participante comer.
listaParticipantes = []

# como são 5 participantes, crio um loop com tamanho de 1 até 5.
for i in range(1, 5 + 1):

    # crio minha variavel porções para armazenar o valor da quantidade separada que cada participante irá consumir.
    porcoes = int(input(""))

    # armazemo os valores da váriavel porções na minha lista 
    listaParticipantes.append(porcoes)
    
    # só determina os participantes na minha lista após o loop estar encerrado.
    if i == 5:

    # para cada índice da minha lista determino um participante e multiplico a quantidade de porções consumidas pelas gramas total de cada porção.
        curupira = listaParticipantes[0] * 300
        boitata = listaParticipantes[1] * 1500
        boto = listaParticipantes[2] * 600
        mapinguari = listaParticipantes[3] * 1000
        lara = listaParticipantes[4] * 150
        donaChica = 225
    # determino a quantidade necessária de mandioca em gramas.
        mandiocaTotal = (curupira + boitata + boto + mapinguari + lara) + donaChica

# saida final.
print(mandiocaTotal)