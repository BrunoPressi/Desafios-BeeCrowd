"""Leia a hora inicial, minuto inicial, hora final e minuto final de um jogo. A seguir calcule a duração do jogo.

Obs: O jogo tem duração mínima de um (1) minuto e duração máxima de 24 horas.

Entrada
Quatro números inteiros representando a hora de início e fim do jogo.

Saída
Mostre a seguinte mensagem: “O JOGO DUROU XXX HORA(S) E YYY MINUTO(S)”."""

tempoDeJogo = str(input(""))
lista_tempoDeJogo = tempoDeJogo.split()

horaInicial = int(lista_tempoDeJogo[0])
minutoInicial = int(lista_tempoDeJogo[1])
horaFinal = int(lista_tempoDeJogo[2])
minutoFinal = int(lista_tempoDeJogo[3])

minutosIniciais = (horaInicial * 60) + minutoInicial
minutosFinais = (horaFinal * 60) + minutoFinal

duracao = minutosFinais - minutosIniciais
horas = duracao // 60
minutos = duracao - (horas * 60)

if duracao < 0:
    duracao = (24 * 60) + duracao
    minutos = duracao % 60
    horas = duracao // 60

elif horaInicial == horaFinal == minutoInicial == minutoFinal:
    print("O JOGO DUROU 24 HORA(S) E 0 MINUTO(S)")
    quit()

print("O JOGO DUROU {} HORA(S) E {} MINUTO(S)".format(horas, minutos))