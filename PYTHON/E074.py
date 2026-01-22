from random import randint
numeros = (randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10))  
print('Os cinco números gerados foram:', end='')
for n in numeros :
    print(f'{n} ', end='') 
print(f'\n O menor númeor foi:{min(numeros)}')
print(f'O maior número foi:{max(numeros)}') 