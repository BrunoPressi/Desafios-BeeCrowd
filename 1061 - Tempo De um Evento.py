"""Pedrinho está organizando um evento em sua Universidade. O evento deverá ser no mês de Abril, iniciando e terminando dentro do mês.
O problema é que Pedrinho quer calcular o tempo que o evento vai durar, uma vez que ele sabe quando inicia e quando termina o evento.

Sabendo que o evento pode durar de poucos segundos a vários dias, você deverá ajudar Pedrinho a calcular a duração deste evento.

Entrada
Como entrada, na primeira linha vai haver a descrição “Dia”, seguido de um espaço e o dia do mês no qual o evento vai começar.
Na linha seguinte, será informado o momento no qual o evento vai iniciar, no formato hh : mm : ss. Na terceira e quarta linha de entrada haverá outra informação no mesmo formato das duas primeiras linhas, indicando o término do evento.

Saída
Na saída, deve ser apresentada a duração do evento, no seguinte formato:

W dia(s)
X hora(s)
Y minuto(s)
Z segundo(s)

Obs: Considere que o evento do caso de teste para o problema tem duração mínima de 1 minuto."""

diaInicial = str(input(""))
momentoInicial = str(input("")) # hh : mm : ss
diaFinal = str(input(""))
momentoFinal = str(input("")) # hh : mm : ss

listaMomentoI = (momentoInicial.split(" : ")) # lista com 3 elementos: # hI : mI : sI, sendo respectivamente, 0, 1, 2.
listaMomentoF = (momentoFinal.split(" : ")) # lista com 3 elementos: # hF : mF : sF, sendo respectivamente, 0, 1, 2.

listaDiaI = (diaInicial.split(" ")) # lista com 2 elementos, sendo o ultimo o dia inicial correspondente.
listaDiaF = (diaFinal.split(" ")) # lista com 2 elementos, sendo o ultimo o dia final correspondente.

dI = int(listaDiaI[1])
dF = int(listaDiaF[1])

valoresIntListaMomentoI = []
for item in listaMomentoI:
    valoresIntListaMomentoI.append(int(item))

hI = valoresIntListaMomentoI[0] # para a hora inicial
mI = valoresIntListaMomentoI[1] # para os minutos iniciais 
sI = valoresIntListaMomentoI[2] # para os segundos iniciais 

segundosIniciais = (dI * 86400) + (hI * 3600) + (mI * 60) + sI # faço a conversão de todos os valores para segundos e realizo a soma total dos mesmos.

valoresIntListaMomentoF = []
for item in listaMomentoF:
    valoresIntListaMomentoF.append(int(item))

hF = valoresIntListaMomentoF[0] # para a hora final
mF =valoresIntListaMomentoF[1] # para os minutos finais 
sF = valoresIntListaMomentoF[2] # para os segundos finais 

segundosFinais = (dF * 86400) + (hF * 3600) + (mF* 60) + sF # faço a conversão de todos os valores para segundos e realizo a soma total dos mesmos.

duracao = segundosFinais - segundosIniciais # determino a duração em segundos, subtraindo segundos finais por segundos iniciais.
dias = duracao // 86400 # determino os dias fazendo a divisão inteira da duração em segundos por 86400.
horas = (duracao // 3600) - (dias * 24) # determino as horas fazendo a divisão inteira da duração por 3600 e descontando as horas dos dias determinados.
minutos = (duracao // 60) - ((dias * 24) * 60) - ((horas * 60)) # determino os minutos fazendo a divisão inteira da duração por 60 e descontando os minutos dos dias e horas determinados.
segundos =  duracao - (dias * 86400) - (horas * 3600) - (minutos * 60) # determino os segundos subtraindo a minha duração, já em segundos, pelos outros valores convertidos em segundos.

print(f"{dias} dia(s)")
print(f"{horas} hora(s)")
print(f"{minutos} minuto(s)")
print(f"{segundos} segundo(s)")
