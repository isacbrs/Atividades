d = int(input("Digite a distância da sua viagem em km:"))
if d >= 200:
    p = d * 0.45
    print("O preço da sua passagem é de R$:{:.2f} reais, pois você irá rodar mais que 200km conosco".format(p))
else:
    p2 = d * 0.50
    print("O preço da sua passagem é de R$:{:.2f} reais".format(p2))     
