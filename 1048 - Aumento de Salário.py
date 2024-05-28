"""A empresa ABC resolveu conceder um aumento de salários a seus funcionários de acordo com a tabela abaixo:


      Salário	           Percentual de Reajuste
    0 - 400.00                      15%
  400.01 - 800.00                   12%
  800.01 - 1200.00                  10%
 1200.01 - 2000.00                  7%
 Acima de 2000.00                   4%

Leia o salário do funcionário e calcule e mostre o novo salário, bem como o valor de reajuste ganho e o índice reajustado, em percentual.

Entrada
A entrada contém apenas um valor de ponto flutuante, com duas casas decimais.

Saída
Imprima 3 linhas na saída: o novo salário, o valor ganho de reajuste (ambos devem ser apresentados com 2 casas decimais) e o percentual de reajuste ganho,"""

salario = float(input(""))

if salario <= 400:
    novo_salario = (salario * 0.15) + salario
    p = 15
elif 400.01 <= salario <= 800:
    novo_salario = (salario * 0.12) + salario
    p = 12
elif 800.01 <= salario <= 1200:
    novo_salario = (salario * 0.10) + salario
    p = 10
elif 1200.01 <= salario <= 2000:
    novo_salario = (salario * 0.07) + salario
    p = 7
elif salario > 2000:
    novo_salario = (salario * 0.04) + salario
    p = 4
print("Novo salario: {:.2f}".format(novo_salario))
print("Reajuste ganho: {:.2f}".format(novo_salario - salario))
print("Em percentual: {} %".format(p))