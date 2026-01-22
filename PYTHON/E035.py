print("-="*20)
print("Analisador de Triângulos")
print("-="*20)
t = float(input("Digite o comprimento da reta1 em cm:"))
u = float(input("Digite o comprimento da reta2 em cm:"))
v = float(input("Digite o comprimento da reta3 em cm:"))
if t < u + v and u < t + v and v < t + u:
    print("¨"*50)
    print("Essas retas formam um triângulo matemático!")
    print("¨"*50)
else:
    print("Não forma um triangulo matemático, mas todas as retas podem formar um triângulo se você imaginar direito")
