"""Neste problema, você deverá ler 3 palavras que definem o tipo de animal possível segundo o esquema abaixo, da esquerda para a direita.
Em seguida conclua qual dos animais seguintes foi escolhido, através das três palavras fornecidas.

Entrada
A entrada contém 3 palavras, uma em cada linha, necessárias para identificar o animal segundo a figura acima, com todas as letras minúsculas.

Saída
Imprima o nome do animal correspondente à entrada fornecida."""

palavra1 = str(input("")).lower()
palavra2 = str(input("")).lower()
palavra3 = str(input("")).lower()

if palavra1 == "vertebrado":
    if palavra2 == "ave":
        if palavra3 == "carnivoro":
            print("aguia")
        if palavra3 == "onivoro":
            print("pomba")
    if palavra2 == "mamifero":
        if palavra3 == "onivoro":
            print("homem")
        if palavra3 == "herbivoro":
            print("vaca")
elif palavra1 == "invertebrado":
    if palavra2 == "inseto":
        if palavra3 == "hematofago":
            print("pulga")
        if palavra3 == "herbivoro":
            print("lagarta")
    if palavra2 == "anelideo":
        if palavra3 == "hematofago":
            print("sanguessuga")
        if palavra3 == "onivoro":
            print("minhoca")