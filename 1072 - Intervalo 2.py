"""Leia um valor inteiro N. Este valor será a quantidade de valores inteiros X que serão lidos em seguida.
Mostre quantos destes valores X estão dentro do intervalo [10,20] e quantos estão fora do intervalo, mostrando essas informações.

Entrada
A primeira linha da entrada contém um valor inteiro N (N < 10000), que indica o número de casos de teste.
Cada caso de teste a seguir é um valor inteiro X (-107 < X <107).
 

Saída
Para cada caso, imprima quantos números estão dentro (in) e quantos valores estão fora (out) do intervalo."""

N = int(input(""))
listaI = []

if N < 10000:
    for i in range(N):
        X = int(input(""))
        listaI.append(X)
        
listaInIntervalo = len([X for X in listaI if (X >= 10 and X <= 20)])
listaForaIntervalo = len([X for X in listaI if (X < 10 or X > 20)])
print(f"{listaInIntervalo} in")
print(f"{listaForaIntervalo} out")