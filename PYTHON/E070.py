total = mais = no = caro = nc = 0
barato = 10000000000000000000000
while True:    
    nome = str(input("Qual o nome do produto:"))
    preço = int(input("Qual o preço do produto:")) 
    cont = input("Quer continuar?").upper()    
    total+= preço
    if preço > int(1000):
        mais+= 1    
    if barato > preço:
        barato = preço
        no = nome
    if caro < preço:
        caro = preço
        nc = nome
    if cont == str('NÃO') or cont == str('N') or cont == str('NAO'):
        break    
print("""Informações:
        No total, essa compra é de: R$:{} reais 
        Cerca de {} produtos custam mais de R$:1.000 reais 
        {} é o produto mais barato da lista, custando R$:{} reais.
        {} é o produto mais caro da lista, custando R$: {} reais""".format(total, mais, no, barato, nc, caro))