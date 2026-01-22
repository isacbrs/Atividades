# COM BIBLIOTECA:
#from math import factorial
#n = int(input("Digite o número que você deseja fatorar: ")) 
#f = factorial(n)
#print("O fatorial de {} é {}".format(n, f))


#                          OU                                 # 
n = int(input("Digite o número que você deseja fatorar:"))
c = n
f = 1
while c > 0:
    f*= c
    c-= 1
print("Resultado:", f) 