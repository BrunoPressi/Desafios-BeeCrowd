"""Leia um valor inteiro, que é o tempo de duração em segundos de um determinado evento em uma fábrica,
e informe-o expresso no formato horas:minutos:segundos.

Entrada
O arquivo de entrada contém um valor inteiro N.

Saída
Imprima o tempo lido no arquivo de entrada (segundos), convertido para horas:minutos:segundos, conforme exemplo fornecido."""

valor_inicial = int(input("")) 

valor_minutos = ((valor_inicial // 60))
valor_horas = (valor_minutos // 60)
valor_segundos = (valor_inicial - (valor_minutos * 60))

print(f"{valor_horas}:{valor_minutos - (valor_horas * 60)}:{valor_segundos}")
