n = int(input("Digite um número inteiro:")) 
if n==2 or n==3 or n==5 or n==7 or n % 2 != 0 and n % 3 != 0 and n % 5 != 0 and n % 7 != 0 and n!= 1: 
    print("É um número primo!")
else:
    print("Não é um número primo!")