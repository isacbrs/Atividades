
k = 0
m = 0
homi = 0
velho = 0
for p in range (1,5):
    nome = input("Qual o nome da {}° pessoa: ".format(p))
    idade = int(input("Qual a idade da {}° pessoa: ".format(p)))
    sexo = int(input("""Qual o sexo da {}° pessoa 
    [1] Homem 
    [2]Mulher
    : """.format(p)))
    k+=idade
    média = int(k/2 )
    if sexo== int(2) and idade<int(18):
        m = m + 1
    if p==1 and sexo==1:
        velho = idade
        homi = nome      
    elif p!=1 and sexo ==1:
        if idade>velho:
            velho = idade
            homi = nome    
print("Á média de idade do grupo é: {}".format(média))
print("O nome do homem mais velho do grupo é:{}".format(homi))    
print("No grupo á um total de {} mulheres com menos de 18 anos".format(m))