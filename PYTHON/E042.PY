print("-="*20)
print("Analisador de Triângulos")
print("-="*20)
t = float(input("Digite o comprimento da reta1 em cm:"))
u = float(input("Digite o comprimento da reta2 em cm:"))
v = float(input("Digite o comprimento da reta3 em cm:"))
k = t < u + v and u < t + v and v < t + u
if k:
    if t == u == v:
        print("Essas retas formam um triângulo equilátero!")
    elif t == u or u == v or t == v:
        print("Essas retas formam um triângulo isósceles!")
    elif t != u != v:
        print("Essas retas formam um triângulo escaleno!")        
else:
    print("Não forma um triangulo matemático!")
