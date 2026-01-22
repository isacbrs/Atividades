n = cont = soma = 0  
n = int(input('Digite um número (77 para parar):')) 
while n!=77:
    cont+=1
    soma+=n
    n = int(input('Digite um número (77 para parar):'))
print(("Você digitou {} números, e a soma total foi de:{}".format(cont, soma)))