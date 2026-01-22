import math
c1 = input("Qual o valor do cateto oposto?")
c2 = input("Qual o valor do cateto adjacente?")
h = math.sqrt(float(c1)**2 + float(c2)**2)
print("O valor da Hipotenusa é: {:.2f}".format(h))