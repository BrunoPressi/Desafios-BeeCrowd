"""Leia a hora inicial e a hora final de um jogo. A seguir calcule a duração do jogo,
sabendo que o mesmo pode começar em um dia e terminar em outro, tendo uma duração mínima de 1 hora e máxima de 24 horas.

Entrada
A entrada contém dois valores inteiros representando a hora de início e a hora de fim do jogo.

Saída
Apresente a duração do jogo conforme exemplo abaixo."""

horas = str(input(""))

lista_horas = horas.split()

hora_inicial = int(lista_horas[0])
hora_final = int(lista_horas[1])

if (hora_inicial >= 1) and (hora_final <= 24):
    if (hora_inicial > hora_final):
        duracao = (24 - hora_inicial) + hora_final
        print(f"O JOGO DUROU {duracao} HORA(S)")
    elif (hora_inicial < hora_final):
        duracao = hora_final - hora_inicial
        print(f"O JOGO DUROU {duracao} HORA(S)")
    elif (hora_inicial == hora_final):
        print("O JOGO DUROU 24 HORA(S)")
elif (hora_inicial == 0 and hora_final == 0):
    print("O JOGO DUROU 24 HORA(S)")