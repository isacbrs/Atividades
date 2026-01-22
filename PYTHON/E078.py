num = []
for p in range (1,6):
    num.append(int(input(f'Digite o {p}° número inteiro:'))) 
print('Os numeros digitados foram:', num)
print(f'O maior valor é {max(num)}, ele está na posição: {num.index(max(num))+1}')
print(f'O menor valor é {min(num)}, ele está na posição: {num.index(min(num))+1}')