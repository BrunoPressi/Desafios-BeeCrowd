"""Leia um valor inteiro correspondente à idade de uma pessoa em dias e informe-a em anos, meses e dias

Obs.: apenas para facilitar o cálculo, considere todo ano com 365 dias e todo mês com 30 dias.
Nos casos de teste nunca haverá uma situação que permite 12 meses e alguns dias, como 360, 363 ou 364.
Este é apenas um exercício com objetivo de testar raciocínio matemático simples.

Entrada
O arquivo de entrada contém um valor inteiro.

Saída
Imprima a saída conforme exemplo fornecido."""

idade_dias = int(input(""))

idade_anos = (idade_dias // 365)
idade_meses = (idade_dias - (idade_anos * 365)) // 30 
idade_dias = (idade_dias - (idade_anos * 365)) - (idade_meses * 30)

print(f"{idade_anos} ano(s)\n{idade_meses} mes(es)\n{idade_dias} dia(s)")