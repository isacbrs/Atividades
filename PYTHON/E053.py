f = input("Digite uma frase:").upper().replace(" ","")
v = f[::-1]
if f == v:
    print("A frase é um palíndromo!")
if f != v:
    print("A frase não é um palíndromo, tente outra frase.")   