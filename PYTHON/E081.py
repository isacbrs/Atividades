num = []
while True:
    num.append((int(input(f'Digite um número inteiro:'))))  
    cont = input('Quer adicionar mais um? [S/N]').upper()
    if cont == str('N'):
        break
print(f'Foram digitados:{len(num)} numeros')
num.sort(reverse=True)    
print('Os números em ordem decrecente são:', num)
if 7 in num:
    print('O número 7 foi digitado')
else:
    print('O número 7 foi digitado')