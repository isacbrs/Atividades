a1 = int(input("Qual é o primeiro termo da PA?"))
r = int(input("Qual é a razão da PA?"))
c = 1
total = 0
mais = 10
while mais !=0:
    total = total + mais
    while c<=total:
        an = a1 + (c-1) * r
        c+= 1
        print("{}->".format(an), end=(''))    
    print(" PAUSA")            
    mais = int(input("Mais quantos termos você quer ver?"))
print("Progresão finalizada, você viu no total {} termos".format(total))