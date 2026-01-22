a1 = int(input("Qual é o primeiro termo da PA?"))
r = int(input("Qual é a razão da PA?"))
c = 1
while c<=10 :
    an = a1 + (c-1) * r
    c+= 1
    print("{}".format(an), end=(''))     
    if c < 11 :
        print("->", end=(''))   
print("FIM")            