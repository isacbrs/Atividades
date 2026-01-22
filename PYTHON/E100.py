from random import randint
from time import sleep


def sorteia(lista):
    print('Sorteando os 5 valores: ', end='')
    for cont in range(0,5):
        n = randint(1,10)
        lista.append(n) 
        print(f'{n} ', end ='', flush = True)
        sleep(0.3) 
    print('PRONTO!')


def somaPar(lista):
    soma = 0
    for valor in lista:
       if valor % 2 == 0:
        soma += valor
    print(f'somando os valores pares de :{lista}, temos o total de:{soma}')


numeros = []
sorteia(numeros)
somaPar(numeros) 