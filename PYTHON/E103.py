def ficha(a, b):
    nome = gols = ''
    if a != '':
        nome = a
    if b != '':
        gols = b         
    print(f'O jogador {nome} fez {gols} gols.')


n = input('Qual o nome do seu Jogador?')
g = input('Quantos Gols ele fez?')
ficha(n, g)