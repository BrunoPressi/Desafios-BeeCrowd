"""Leia um valor de ponto flutuante com duas casas decimais. Este valor representa um valor monetário.
A seguir, calcule o menor número de notas e moedas possíveis no qual o valor pode ser decomposto.
As notas consideradas são de 100, 50, 20, 10, 5, 2. As moedas possíveis são de 1, 0.50, 0.25, 0.10, 0.05 e 0.01. A seguir mostre a relação de notas necessárias.

Entrada
O arquivo de entrada contém um valor de ponto flutuante N (0 ≤ N ≤ 1000000.00).

Saída
Imprima a quantidade mínima de notas e moedas necessárias para trocar o valor inicial, conforme exemplo fornecido.

Obs: Utilize ponto (.) para separar a parte decimal."""

valor = float(input(""))

if (0 <= valor <= 1000000.00):

    # notas possíveis:
    notas100 = valor // 100
    notas50 = (valor % 100) // 50
    notas20 = ((valor % 100) % 50) // 20
    notas10 = (((valor % 100) % 50) % 20) // 10
    notas5 = ((((valor % 100) % 50) % 20) % 10) // 5
    notas2 = (((((valor % 100) % 50) % 20) % 10) % 5 ) // 2

    notasTotais = (notas100 * 100) + (notas50 * 50) + (notas20 * 20) + (notas10 * 10) + (notas5 * 5) + (notas2 * 2)

    #moedas possíveis:
    restoValor = (valor - notasTotais)

    moeda1 = restoValor // 1
    moeda050 = ((restoValor % 1) * 100) // 50
    moeda025 = (((restoValor % 1) * 100) % 50) // 25
    moeda010 = ((((restoValor % 1) * 100) % 50) % 25) // 10
    moeda005 = (((((restoValor % 1) * 100) % 50) % 25) % 10) // 5
    moeda001 = ((((((restoValor % 1) * 100) % 50) % 25) % 10) % 5) // 1

txt1 = "{:.0f} nota(s) de R$ 100.00"
txt2 = "{:.0f} nota(s) de R$ 50.00"
txt3 = "{:.0f} nota(s) de R$ 20.00"
txt4 = "{:.0f} nota(s) de R$ 10.00"
txt5 = "{:.0f} nota(s) de R$ 5.00"
txt6 = "{:.0f} nota(s) de R$ 2.00"

txt7 = "{:.0f} moeda(s) de R$ 1.00"
txt8 = "{:.0f} moeda(s) de R$ 0.50"
txt9 = "{:.0f} moeda(s) de R$ 0.25"
txt10 = "{:.0f} moeda(s) de R$ 0.10"
txt11 = "{:.0f} moeda(s) de R$ 0.05"
txt12 = "{:.0f} moeda(s) de R$ 0.01"

print("NOTAS:")
print(txt1.format(notas100))
print(txt2.format(notas50))
print(txt3.format(notas20))
print(txt4.format(notas10))
print(txt5.format(notas5)) 
print(txt6.format(notas2)) 
print("MOEDAS:")
print(txt7.format(moeda1)) 
print(txt8.format(moeda050))
print(txt9.format(moeda025))
print(txt10.format(moeda010))
print(txt11.format(moeda005))
print(txt12.format(moeda001))