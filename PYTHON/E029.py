v = int(input("Digite a velocidade máxima atingida pelo carro:"))
m = (v-80)*7
if v > 80:
    print("Você ultrapassou o limite de 80km por hora e foi multado em R$:{} reais".format(m))
else:
    print("Você está dentro do limite de velocidade. Tenha um bom dia!")    