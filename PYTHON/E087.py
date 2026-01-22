matriz = [[],[],[]]
pares = tres = maior = 0
for p in range (1,10):
    num = int(input(f'Digite o {p}° número inteiro:'))
    if p == 3 or p==6 or p==9:
        tres+=num
    if num % 2 == 0:
        pares+=num
    if p <=3:
        matriz[0].append(num)
    elif p > 3 and p <= 6:
        matriz[1].append(num)
        if maior < num:
            maior = num    
    else:
        matriz[2].append(num)           
print(f"""Á matriz é:\n{matriz[0]}\n{matriz[1]}\n{matriz[2]}""")
print(f'A soma dos valores pares são: {pares}')
print(f'A soma dos valores da 3° coluna é :{tres}')
print(f'O maior valor da 2° linha é: {maior}')