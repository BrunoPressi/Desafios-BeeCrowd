"""Tacógrafos são dispositivos instalados em determinados tipos de veículos, que registram a velocidade, tempo e distância percorrida por tal veículo.
É utilizada principalmente em veículos de transporte coletivo e de transporte de cargas,
assim ajudando a evitar abusos de velocidade por parte dos motoristas.

A empresa SBC (Sociedade Brasileira dos Caminhoneiros) decidiu encomendar uma versão um pouco mais básica (e barata)
para seus associados não precisarem gastar tanto na instalação desses aparelhos.
Essas versões modificadas registram apenas os intervalos de tempo e as velocidades médias do caminhão naqueles intervalos.

Apesar das restrições dos aparelhos novos, a SBC quer poder saber qual foi a distância percorrida pelos caminhões.
Você deverá escrever um programa que recebe uma série de intervalos de tempo com suas respectivas velocidades médias
e calcula qual foi a distância total percorrida pelo caminhão de acordo com o tacógrafo.

Entrada
A primeira linha da entrada contém um inteiro N (1 ≤ N ≤ 1000) representando a quantidade de intervalos de tempo registrados no tacógrafo.
As N linhas seguintes descrevem os intervalos de tempo. Cada uma dessas linhas possui dois inteiros T e V (1 ≤ T ≤ 100, 0 ≤ V ≤ 120),
que representam, respectivamente o tempo decorrido (em horas) e a velocidade média (em quilômetros por hora) no intervalo de tempo.

Saída
Seu programa deve imprimir uma única linha, contendo um único número inteiro representando a distância total percorrida, em quilômetros."""

quantidadeDeIntervalos = int(input(""))

# váriavel representnado distância total percorrida, inicialmente 0.
distanciaTotal = 0

# condição para verificar se a quantidade de intervalos de tempos corresponde ao requisito passado no enunciado.
if 1 <= quantidadeDeIntervalos <= 1000:

    # caso a condição seja verdadeira, será criado um loop com range de 1 até o tamanho da quantidade de intervalos de tempo.
    for i in range(1 , quantidadeDeIntervalos + 1):

        # essa váriavel armazena duas strings, correspondendo a: tempo decorrido(hrs) e velocidade média(km/hr), respectivamente.
        intervalosDeTempo = str(input(""))

        # armazena meus valores digitados na váriavel acima em uma lista, contendo dois índices, [0] = tempo decorrido(hrs) e [1] = velocidade média(km/hr).
        listaIntervaloDeTempos = intervalosDeTempo.split()

        # convertendo os valores lista acima que estavam em strings para inteiros. Adicionando os mesmos as suas respectivas váriaveis.
        tempoDecorrido = int(listaIntervaloDeTempos[0])
        velocidadeMedia = int(listaIntervaloDeTempos[1])

        # condição para checar se os valores correspondem com o requisito do enunciado.
        if (1 <= tempoDecorrido <= 100) and (0 <= velocidadeMedia <= 120):

            # fórmula para calcular a distância em um intervalo de tempo.
            distancia = velocidadeMedia * tempoDecorrido

            # calculo da distância total percorida de acordo com a quantidade de intervalos de tempos.
            distanciaTotal += distancia

print(distanciaTotal)