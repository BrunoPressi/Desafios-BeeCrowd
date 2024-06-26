"""A Federação Gaúcha de Futebol contratou você para escrever um programa para fazer uma estatística do resultado de vários GRENAIS.
Escreva um programa para ler o número de gols marcados pelo Inter e pelo Grêmio em um GRENAL.
Logo após escrever a mensagem "Novo grenal (1-sim 2-nao)" e solicitar uma resposta.
Se a resposta for 1, o algoritmo deve ser executado novamente solicitando o número
de gols marcados pelos times em uma nova partida, caso contrário deve ser encerrado imprimindo:

- Quantos GRENAIS fizeram parte da estatística.
- O número de vitórias do Inter.
- O número de vitórias do Grêmio.
- O número de Empates.
- Uma mensagem indicando qual o time que venceu o maior número de GRENAIS (ou "Nao houve vencedor", caso termine empatado).

Entrada
O arquivo de entrada contém 2 valores inteiros, correspondentes aos gols marcados pelo Inter e pelo Grêmio respectivamente.
Em seguida háverá um inteiro (1 ou 2), correspondente à repetição do programa.

Saída
Após cada leitura dos gols, deve ser impressa a mensagem "Novo grenal (1-sim 2-nao)".
Quando o algoritmo for encerrado devem ser mostradas as estatísticas conforme a descrição apresentada acima.
Obs: a palavra "Gremio" deve ser impressa sem acento, conforme o exemplo abaixo."""

nGrenais = 0
nVitoriasInter = 0
nVitoriasGremio = 0
empates = 0

# enquanto meu loop for verdadeiro:
while True:
    golsInter, golsGremio = map(int, input("").split())
    nGrenais += 1

    # armazeno as estatísticas em suas váriaveis.
    if golsInter > golsGremio: nVitoriasInter += 1
    elif golsGremio > golsInter: nVitoriasGremio += 1
    else: empates += 1

    print("Novo grenal (1-sim 2-nao)")
    
    # condição para verificar se o loop continua ou não.
    repeticao = int(input(("")))

    # loop continua.
    if repeticao == 1:
        continue
    
    # condição de parada do loop.
    if repeticao == 2:
        break

# saída final.
print(f"{nGrenais} grenais")
print(f"Inter: {nVitoriasInter}")
print(f"Gremio: {nVitoriasGremio}")
print(f"Empates: {empates}")

if nVitoriasGremio == nVitoriasInter: print("Nao houve vencedor")
elif nVitoriasGremio > nVitoriasInter: print("Gremio venceu mais")
else: print("Inter venceu mais")