num = []
p = 0
while True:
    p+=1
    n = (int(input(f'Digite o {p}° número inteiro:')))
    if n in num:
        print('Esse número já foi adicionado')
    else:    
        num.append(n)    
    cont = input('Quer adicionar mais um? [S/N]').upper()
    if cont == str('N'):
        break
num.sort()
print(f'Os numeros digitados foram:{num}')