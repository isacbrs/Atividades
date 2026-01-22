from time import sleep
def maior(* num):
    cont = maior = 0
    print('\nanalisando os valores!! ')
    for valor in num:
        print(valor, end=' ', flush = True)
        sleep(0.3)
        if cont == 0:
           maior = valor
        else:
            if valor > maior:
                maior = valor
    print(f'\nO maior número é: {maior}')
    print('-='*30)


#Programa rodando
maior(2, 9, 4, 5, 7, 2)
maior(1, 2)
maior(6)
maior()