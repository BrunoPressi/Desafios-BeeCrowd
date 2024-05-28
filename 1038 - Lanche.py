"""Com base na tabela abaixo, escreva um programa que leia o código de um item e a quantidade deste item.
A seguir, calcule e mostre o valor da conta a pagar.

CODIGO      ESPECIFICACAO       PREÇO
   1        Cachorro Quente     R$ 4.00
   2           X-Salada         R$ 4.50
   3           X-Bacon          R$ 5.00
   4        Torrada Simples     R$ 2.00 
   5         Refrigerante       R$ 1.50

Entrada
O arquivo de entrada contém dois valores inteiros correspondentes ao código e à quantidade de um item conforme tabela acima.

Saída
O arquivo de saída deve conter a mensagem "Total: R$ " seguido pelo valor a ser pago, com 2 casas após o ponto decimal."""

pedido = str(input("")) 

lista_pedido = pedido.split()

codigoPedido = int(lista_pedido[0])
quantidadePedido = int(lista_pedido[1])


if (codigoPedido == 1):
    valor = quantidadePedido * 4.00
    print("Total: R$ {:.2f}".format(valor))
elif (codigoPedido == 2):
    valor = quantidadePedido * 4.50
    print("Total: R$ {:.2f}".format(valor))
elif (codigoPedido == 3):
    valor = quantidadePedido * 5.00
    print("Total: R$ {:.2f}".format(valor))
elif (codigoPedido == 4):
    valor = quantidadePedido * 2.00
    print("Total: R$ {:.2f}".format(valor))
elif (codigoPedido == 5):
    valor = quantidadePedido * 1.50
    print("Total: R$ {:.2f}".format(valor))