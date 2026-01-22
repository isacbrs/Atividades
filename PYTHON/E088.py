from random import randint
jogo = list()
lista = list()
print('JOGA NA MEGA') 
j = int(input('Quantos jogos você quer gerar:'))
print(f'SORTEANDO {j} JOGOS')
for p in range (0, j):
    cont = 0
    while True:
        num = randint(1,60)
        if num not in lista:
            lista.append(num)
            cont+=1
        if cont >=6:
         break
    lista.sort()
    jogo.append(lista[:])
    lista.clear()
print(f'Os números sorteados foram:{jogo}')    
print('BOA SORTE')