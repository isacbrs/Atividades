from módulos import moeda
from módulos import dado
p = float(input('Digite o preço R$:'))
d = dado.leiadinheiro(p)
moeda.resumo(d)