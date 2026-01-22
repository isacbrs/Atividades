m = 0
p = 0
h = 0
while True:    
    sexo = str(input("Homem ou Mulher?")).upper()
    idade = int(input("Idade da pessoa:")) 
    cont = input("Quer continuar?").upper()
    if sexo == str('MULHER') and idade < 20:
        m+= 1
    if sexo == str('HOMEM'):
        h+= 1
    if idade > 18:
        p+= 1    
    if cont == str('NÃO') or cont == str('N') or cont == str('NAO'):
        break
print("""No total:
        {} pessoas tem mais de 18 anos 
        {} homens foram cadastrados 
        {} mulheres tem menos de 20 anos.""".format(p, h, m))