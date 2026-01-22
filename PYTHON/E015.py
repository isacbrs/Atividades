c = input("Qual foi o carro alugado?") #serve pra nada, só pra tornar mais imercivo
d = input("Quantos dias o carro foi alugado?")
k = input("Quantos km foram rodados?")
t = (60*int(d)+0.15*int(k))
print("O valor total á pagar é de R$:{:.2f} reais".format(t))