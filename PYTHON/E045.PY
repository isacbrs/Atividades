import random

print("-="*30)
print("Vamos jogar jokenpô? Só acaba quando você ganhar!")
print('-='*30)

itens = ['Pedra', 'Papel', 'Tesoura']
jogadas = {1: 'Pedra', 2: 'Papel', 3: 'Tesoura'}

while True:
    computador = random.choice(itens)
    
    jogador = int(input("""Qual é a sua jogada? 
[1]PEDRA
[2]PAPEL
[3]TESOURA
:"""))        
    jogada_player = jogadas[jogador]
    print("-="*30)
    print("Computador jogou: {}".format(computador))
    print("-="*30)
        
        # Verifica se o jogador ganhou
    if (jogada_player == 'Pedra' and computador == 'Tesoura') or \
           (jogada_player == 'Papel' and computador == 'Pedra') or \
           (jogada_player == 'Tesoura' and computador == 'Papel'):
            print("""JOGADOR VENCEU!
                  \033[1;31mFIM DO GAME\033[m""")
            break
    elif jogada_player == computador:
        print("EMPATE!")
    else:
        print("COMPUTADOR VENCEU!")