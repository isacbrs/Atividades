import random
print("-="*30)
print("Vamos jogar impar ou par? Só acaba quando você perde!")
print('-='*30)
itens = ['impar', 'par']
vi = 0
while True:
    jogador = str(input("""Impar ou Par?""")).lower()
    numdojogador = int(input('Digite um número:'))
    computador = random.choice(itens)
    numdocomputador = random.randint(0,10) 
    if computador == jogador:
        while True:
           computador = random.choice(itens)
           if computador != jogador:
               break
    print("Computador escolheu: {} e disse {}".format(computador, numdocomputador))
    num = numdojogador + numdocomputador  
        # Verifica se o jogador ganho
    if jogador == str('par') and num % 2 == 0:
        print('VOCÊ VENCEU!')
        vi+= 1
    elif jogador == str('impar') and num % 2 != 0:
        print("VOCÊ VENCEU")
        vi+= 1
    elif computador == str('par') and num % 2 == 0:
        print('COMPUTADOR VENCEU!')
        break
    elif computador == str('impar') and num % 2 != 0:
        print("COMPUTADOR VENCEU!")
        break
    else:
        print('EMPATE')
print(f"Fim de jogo, você ganhou {vi} vezes")   