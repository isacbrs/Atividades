par = []
impar = []
num = []
while True:
    n = (int(input(f'Digite um número inteiro:')))
    num.append(n)  
    if n % 2 == 0:
       par.append(n)
    else:
        impar.append(n)   
    cont = input('Quer adicionar mais um? [S/N]').upper()
    if cont == str('N'):
        break
print('Os números digitados foram:', num)
print(f'Os números parés são:{par}')
print('Os númeors impares são:', impar)