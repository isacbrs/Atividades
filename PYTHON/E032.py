# não sei como colocar isso: �, só apareceu, então to guardando aqui
from datetime import date
ano = int(input("Qual ano você quer anaalisar?"))
if ano == 0:
    ano = date.today().year
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print("O ano de {} é bissexto.".format(ano))
else:
    print("O ano de {} não é bissexto.".format(ano))    