s = 0
v = 0
for c in range(0,7):
    k = int(input("Quais são os anos de nascimento? Digite um por um:"))
    for c in range(1):
        m = 2025 - k
        if m >= 18:
            print("Maior de idade")
            s = s + 1
        else:
            print("Menor de idade")
            v = v + 1
print("Ao todo teve {} pessoas maiores de idade e {} pessoas menores de idade".format(s,v))           