"""Péricles é um rapaz que tem um interesse único por história. Utilizando seu atualizadíssimo navegador de internet rapoza cromada,
conheceu até os sitios mais remotos e obscuros atrás de informações sobre a mitologia grega.

Por ironia do destino, o navegador de Péricles acabou sendo infectado por um malware com uma caracterísica peculiar:
cada vez que Péricles fechava uma aba no seu navegador, outras duas abas apareciam! No entanto,
quando Péricles clicou sem querer em uma das propagandas de uma aba, percebeu que,
por um erro do navegador, a aba foi encerrada (sem abrir outras abas).
Por causa do malware, todas as abas possuem irritantes propagandas.

Sua tarefa é descobrir com quantas abas que o navegador de Péricles ficou,
sabendo o número inicial de abas e a sequência de ações de Péricles.
As ações podem ser fechou (quando Péricles fechou uma aba) ou clicou (quando Péricles clicou em uma propaganda).

Entrada
A entrada é iniciada por uma linha contendo dois números inteiros positivos, N e M (0 < N, M < 500),
representando o número inicial de abas e o número de ações de Péricles.
Cada linha subsequente contém uma ação (fechou ou clicou). Naturalmente, o número de abas é sempre maior ou igual a zero.

Saída
A saída deve ser uma linha contendo o número final de abas."""

N, M = str(input("")).split()

# faço a conversão dos valores N e M para inteiros.
N = int(N) # N = número inicial de abas.
M = int(M) # M = número de ações.

if (N > 0 ) and (M < 500):

    # loop de acordo com o valor na váriavel M (número de ações).
    for acoes in range(1, M + 1):

        # váriavel que terá como entrada apenas: "fechou" ou "clicou", representando o tipo de ação.
        acao = str(input(""))

        # cada vez que a ação será "fechou" uma aba será fechada e duas novas abas serão abertas, portanto: 
        if acao == "fechou":
            N += 1
        elif acao == "clicou":
            N -= 1
            
#saída final:
print(N)