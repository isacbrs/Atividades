a1 = int(input("Qual é o primeiro termo da PA?"))
r = int(input("Qual é a razão da PA?"))
for c in range(1, 11):
    an = a1 + (c-1) * r
    print("{}".format(an))
