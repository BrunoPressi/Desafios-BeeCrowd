"""Leia quatro números (N1, N2, N3, N4), cada um deles com uma casa decimal, correspondente às quatro notas de um aluno.
Calcule a média com pesos 2, 3, 4 e 1, respectivamente, para cada uma destas notas e mostre esta média acompanhada pela mensagem "Media: ".
Se esta média for maior ou igual a 7.0, imprima a mensagem "Aluno aprovado.". Se a média calculada for inferior a 5.0, imprima a mensagem
"Aluno reprovado.". Se a média calculada for um valor entre 5.0 e 6.9, inclusive estas, o programa deve imprimir a mensagem "Aluno em exame.".

No caso do aluno estar em exame, leia um valor correspondente à nota do exame obtida pelo aluno.
Imprima então a mensagem "Nota do exame: " acompanhada pela nota digitada.
Recalcule a média (some a pontuação do exame com a média anteriormente calculada e divida por 2).
e imprima a mensagem "Aluno aprovado." (caso a média final seja 5.0 ou mais ) ou "Aluno reprovado.",
(caso a média tenha ficado 4.9 ou menos). Para estes dois casos (aprovado ou reprovado após ter pego exame)
apresente na última linha uma mensagem "Media final: " seguido da média final para esse aluno.

Entrada
A entrada contém quatro números de ponto flutuante correspendentes as notas dos alunos.

Saída
Todas as respostas devem ser apresentadas com uma casa decimal.
As mensagens devem ser impressas conforme a descrição do problema.
Não esqueça de imprimir o enter após o final de cada linha, caso contrário obterá "Presentation Error"."""

notas = str(input(""))

lista_notas = notas.split()

N1 = float(lista_notas[0]) # peso 2
N2 = float(lista_notas[1]) # peso 3
N3 = float(lista_notas[2]) # peso 4
N4 = float(lista_notas[3]) # peso 1

# A fórmula para calcular a média ponderada é: (soma das notas * peso das notas) / total dos pesos

media_ponderada = ((N1 * 2) + (N2 * 3) + (N3 * 4) + (N4)) / 10
print("Media: {:.1f}".format(media_ponderada))

if (media_ponderada >= 7):
    print("Aluno aprovado.")
elif (media_ponderada < 5):
    print("Aluno reprovado.")
elif (media_ponderada > 4.9) and (media_ponderada < 7.0):
    print("Aluno em exame.")
    N5 = float(input(""))
    print("Nota do exame: {:.1f}".format(N5))
    media_final = (N5 + media_ponderada) / 2
    if (media_final >= 5):
        print("Aluno aprovado.")
        print("Media final: {:.1f}".format(media_final))
    elif (media_final <= 4.9):
        print("Aluno reprovado.")
        print("Media final: {:.1f}".format(media_final))