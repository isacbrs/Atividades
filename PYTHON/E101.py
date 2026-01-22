def voto(v=0):
    n = 2025 - v
    if n < 16:
        print('NEGADO!')
    if n >=16 and n < 18:
        print('OPCIONAL!')
    if n >= 18:
        print('OBRIGATÓRIO!')


print('Você pode vota?')
print('-='*30)
ano = int(input('Seu ano de nascimento:'))
voto(ano)