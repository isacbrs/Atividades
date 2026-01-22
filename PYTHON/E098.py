from time import sleep


def contador(i, f,  p):
    if p < 0:
        p*= -1
    elif p == 0:
        p == 1
    print(f'\nContagem de {i} até {f} de {p} em {p}')
    if i < f:
        cont = i
        while cont<=f:
            print(f'{cont}', end=' ', flush=True)
            sleep(0.5)
            cont+= p 
    else:
        cont = i
        while cont>=f:
            print(f'{cont}', end=' ', flush = True)
            sleep(0.5)
            cont-=p


#PROGRAMA RODANDO
contador(1, 10, 1)
contador(10, 0, 2)
print()
print('-='*30)
print('Agora você decide!')
ini = int(input('Início:'))
fim = int(input('Fim:'))
passo = int(input('Passo:'))
contador(ini, fim, passo)